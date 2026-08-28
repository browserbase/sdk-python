#!/usr/bin/env -S uv run python
"""Per-file Downloads API example.

`bb.sessions.downloads.list(session_id)` returns one zip archive containing every
file a session downloaded (see `playwright_downloads.py`). Browserbase also
documents a per-file API under `/v1/downloads`: list a session's downloads with
filters and pagination, fetch one file's metadata or bytes by id, delete one by
id. Those endpoints are not part of the generated SDK yet:

    https://docs.browserbase.com/features/downloads
    https://docs.browserbase.com/reference/api/list-downloads

This example reaches them through the client's `get()` escape hatch and
`make_request_options()`, the same calls the generated resources use, then checks
the fetched bytes against the `size` and SHA-256 `checksum` from the listing.
"""

import re
import time
import hashlib
import tempfile
from typing import List
from pathlib import Path
from datetime import datetime

from pydantic import Field as FieldInfo
from playwright.sync_api import Playwright, sync_playwright

from examples import BROWSERBASE_PROJECT_ID, bb
from browserbase import BaseModel
from browserbase._response import BinaryAPIResponse
from browserbase._base_client import make_request_options

# The zip endpoint suffixes each entry with a Unix timestamp (sandstorm-<ms>.mp3);
# the per-file API reports the original filename (sandstorm.mp3). Accept both.
download_re = re.compile(r"sandstorm(-\d{13})?\.mp3")
EXPECTED_FILE_SIZE = 6137541

# Files sync to Browserbase storage shortly after the browser finishes writing
# them, so the listing can lag the Playwright download event by a few seconds.
POLL_TIMEOUT_SECONDS = 30.0
POLL_INTERVAL_SECONDS = 2.0


class Download(BaseModel):
    """One entry from `GET /v1/downloads`, as documented by Browserbase."""

    id: str
    session_id: str = FieldInfo(alias="sessionId")
    filename: str
    mime_type: str = FieldInfo(alias="mimeType")
    size: int
    checksum: str
    """SHA-256 of the file contents, hex encoded."""
    created_at: datetime = FieldInfo(alias="createdAt")


class DownloadListResponse(BaseModel):
    downloads: List[Download]
    total: int
    limit: int
    offset: int


def list_downloads(session_id: str) -> DownloadListResponse:
    # Other supported query params: filename, mimeType, minSize, maxSize,
    # createdAfter, createdBefore, offset. limit defaults to 20, max 100.
    return bb.get(
        "/v1/downloads",
        options=make_request_options(extra_query={"sessionId": session_id, "limit": 100}),
        cast_to=DownloadListResponse,
    )


def wait_for_downloads(session_id: str) -> DownloadListResponse:
    deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
    while True:
        listing = list_downloads(session_id)
        if listing.total > 0:
            return listing
        if time.monotonic() >= deadline:
            raise Exception(f"No downloads listed for session {session_id} after {POLL_TIMEOUT_SECONDS:.0f}s")
        time.sleep(POLL_INTERVAL_SECONDS)


def fetch_download(download_id: str) -> BinaryAPIResponse:
    # Without this Accept header the endpoint returns the JSON metadata instead.
    return bb.get(
        f"/v1/downloads/{download_id}",
        options=make_request_options(extra_headers={"Accept": "application/octet-stream"}),
        cast_to=BinaryAPIResponse,
    )


def run(playwright: Playwright) -> None:
    # Create a session on Browserbase
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
    assert session.id is not None
    assert session.status == "RUNNING", f"Session status is {session.status}"

    # Connect to the remote session
    browser = playwright.chromium.connect_over_cdp(session.connect_url)
    context = browser.contexts[0]
    page = context.pages[0]

    # Downloads only sync to Browserbase with exactly this configuration:
    # downloadPath must be "downloads" and eventsEnabled must be true.
    client = context.new_cdp_session(page)
    client.send(  # pyright: ignore
        "Browser.setDownloadBehavior",
        {
            "behavior": "allow",
            "downloadPath": "downloads",
            "eventsEnabled": True,
        },
    )

    # Trigger a download and wait for the browser to finish it
    page.goto("https://browser-tests-alpha.vercel.app/api/download-test")
    with page.expect_download() as download_info:
        page.locator("#download").click()
    download = download_info.value

    download_error = download.failure()
    if download_error:
        raise Exception(f"Download for session {session.id} failed: {download_error}")

    page.close()
    browser.close()

    # 1. List the session's downloads, polling until the file has synced
    listing = wait_for_downloads(session.id)
    print(f"Listed {listing.total} download(s) for the session:")
    for item in listing.downloads:
        print(f"  {item.filename}  {item.mime_type}  {item.size} bytes  sha256={item.checksum}")

    entry = next((item for item in listing.downloads if download_re.match(item.filename)), None)
    if entry is None:
        raise Exception(
            f"Session {session.id} has no download matching '{download_re.pattern}': "
            f"{[item.filename for item in listing.downloads]}"
        )

    # 2. Fetch that one file by id and write it to disk
    out_dir = Path(tempfile.mkdtemp(prefix="browserbase-downloads-"))
    out_path = out_dir / entry.filename
    fetch_download(entry.id).write_to_file(out_path)

    # 3. Check the bytes on disk against the listing's size and checksum
    data = out_path.read_bytes()
    actual_checksum = hashlib.sha256(data).hexdigest()
    assert len(data) == entry.size, f"Expected {entry.size} bytes per the listing, but got {len(data)}"
    assert len(data) == EXPECTED_FILE_SIZE, f"Expected file size {EXPECTED_FILE_SIZE}, but got {len(data)}"
    assert actual_checksum == entry.checksum, f"Expected sha256 {entry.checksum}, but got {actual_checksum}"

    print(f"Wrote {entry.filename} ({len(data)} bytes) to {out_path}")
    print("Downloads API example passed successfully!")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
