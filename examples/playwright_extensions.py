import os
import zipfile
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, Playwright
from browserbase.types.extension import Extension
from browserbase.types.session import Session
from examples import (
    BROWSERBASE_API_KEY,
    BROWSERBASE_PROJECT_ID,
    BROWSERBASE_CONNECT_URL,
    bb,
)
from io import BytesIO

PATH_TO_EXTENSION = (
    Path.cwd() / "examples" / "packages" / "extensions" / "browserbase-test"
)


def zip_extension(path: Path = PATH_TO_EXTENSION, save_local: bool = False) -> BytesIO:
    """
    Create an in-memory zip file from the contents of the given folder.
    Mark save_local=True to save the zip file to a local file.
    """
    # Ensure we're looking at an extension
    assert "manifest.json" in os.listdir(
        path
    ), "No manifest.json found in the extension folder."

    # Create a BytesIO object to hold the zip file in memory
    memory_zip = BytesIO()

    # Create a ZipFile object
    with zipfile.ZipFile(memory_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        # Recursively walk through the directory
        for root, _, files in os.walk(path):
            for file in files:
                # Create the full file path
                file_path = os.path.join(root, file)
                # Calculate the archive name (path relative to the root directory)
                archive_name = os.path.relpath(file_path, path)
                # Add the file to the zip
                zf.write(file_path, archive_name)

    if save_local:
        with open(f"{path}.zip", "wb") as f:
            f.write(memory_zip.getvalue())

    return memory_zip


def create_extension():
    zip_data = zip_extension(save_local=True)
    extension: Extension = bb.extensions.create(
        file=("extension.zip", zip_data.getvalue())
    )
    return extension.id


def get_extension(id: str) -> Extension:
    return bb.extensions.retrieve(id)


def delete_extension(id: str):
    bb.extensions.delete(id)


def run(playwright: Playwright):
    extension_id = None

    # Create extension
    extension_id = create_extension()
    print(f"Created extension with ID: {extension_id}")

    # Get extension
    extension = get_extension(extension_id)
    print(f"Retrieved extension: {extension}")

    # Use extension
    session: Session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
        extension_id=extension.id,
    )

    browser = playwright.chromium.connect_over_cdp(
        f"{BROWSERBASE_CONNECT_URL}?apiKey={BROWSERBASE_API_KEY}&sessionId={session.id}"
    )
    context = browser.contexts[0]
    page = context.pages[0]

    console_messages: list[str] = []
    page.on("console", lambda msg: console_messages.append(msg.text))

    page.goto("https://www.browserbase.com/")

    # Wait for the extension to load and log a message
    start = time.time()
    while time.time() - start < 10:
        if "browserbase test extension image loaded" in console_messages:
            break
    assert (
        "browserbase test extension image loaded" in console_messages
    ), f"Expected message not found in console logs. Messages: {console_messages}"

    page.close()
    browser.close()

    # Use extension with proxies
    session_with_proxy: Session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
        extension_id=extension_id,
        proxies=True,
    )

    browser = playwright.chromium.connect_over_cdp(
        f"{BROWSERBASE_CONNECT_URL}?apiKey={BROWSERBASE_API_KEY}&sessionId={session_with_proxy.id}"
    )
    context = browser.contexts[0]
    page = context.pages[0]

    console_messages: list[str] = []
    page.on("console", lambda msg: console_messages.append(msg.text))

    page.goto("https://www.browserbase.com/")

    # Wait for the extension to load and log a message (longer timeout for proxies)
    start = time.time()
    while time.time() - start < 10:
        if "browserbase test extension image loaded" in console_messages:
            break
    assert (
        "browserbase test extension image loaded" in console_messages
    ), f"Expected message not found in console logs. Messages: {console_messages}"

    page.close()
    browser.close()

    # Delete extension
    delete_extension(extension_id)
    print(f"Deleted extension with ID: {extension_id}")

    # Verify deleted extension is unusable
    try:
        get_extension(extension_id)
        raise AssertionError("Expected to fail when retrieving deleted extension")
    except Exception as e:
        print(f"Failed to get deleted extension as expected: {str(e)}")

    try:
        bb.sessions.create(
            project_id=BROWSERBASE_PROJECT_ID,
            extension_id=extension_id,
        )
        raise AssertionError(
            "Expected to fail when creating session with deleted extension"
        )
    except Exception as e:
        print(f"Failed to create session with deleted extension as expected: {str(e)}")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
