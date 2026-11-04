"""Contract tests against the generated SDK, without API credentials or a mock server."""

from __future__ import annotations

import asyncio
from typing import Iterator, AsyncIterator
from pathlib import Path
from typing_extensions import override

import httpx
import pytest

from browserbase import Browserbase, NotFoundError, AsyncBrowserbase
from browserbase.types import DownloadListParams
from browserbase.pagination import SyncOffsetPage, AsyncOffsetPage
from browserbase.types.download import Download

SESSION_ID = "00000000-0000-4000-8000-000000000001"
FILTERS: DownloadListParams = {
    "session_id": SESSION_ID,
    "filename": "a report & summary.json",
    "mime_type": "application/json",
    "min_size": 0,
    "max_size": 1024,
    "created_after": "2026-09-01T00:00:00Z",
    "created_before": "2026-09-02T00:00:00Z",
    "limit": 2,
    "offset": 2,
}
WIRE_FILTERS = {
    "sessionId": SESSION_ID,
    "filename": FILTERS["filename"],
    "mimeType": "application/json",
    "minSize": "0",
    "maxSize": "1024",
    "createdAfter": FILTERS["created_after"],
    "createdBefore": FILTERS["created_before"],
    "limit": "2",
    "offset": "2",
}


def download(id: str) -> dict[str, object]:
    return {
        "id": id,
        "sessionId": SESSION_ID,
        "filename": "report.json",
        "mimeType": "application/json",
        "size": 12,
        "checksum": "a" * 64,
        "createdAt": "2026-09-01T00:00:00Z",
    }


class Chunks(httpx.SyncByteStream, httpx.AsyncByteStream):
    def __init__(self, chunks: tuple[bytes, ...] = (b"first", b"last"), error: BaseException | None = None) -> None:
        self.chunks = chunks
        self.error = error
        self.reads = 0
        self.closed = False

    @override
    def __iter__(self) -> Iterator[bytes]:
        for chunk in self.chunks:
            self.reads += 1
            yield chunk
        if self.error:
            raise self.error

    @override
    async def __aiter__(self) -> AsyncIterator[bytes]:
        for chunk in self:
            yield chunk

    @override
    def close(self) -> None:
        self.closed = True

    @override
    async def aclose(self) -> None:
        self.close()


class API:
    def __init__(
        self, *, stream: Chunks | None = None, content_type: str = "application/octet-stream", empty: bool = False
    ) -> None:
        self.requests: list[httpx.Request] = []
        self.stream = stream
        self.content_type = content_type
        self.empty = empty

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if request.url.path == "/v1/downloads":
            offset = int(request.url.params.get("offset", "0"))
            return httpx.Response(
                200,
                json={
                    "downloads": [] if self.empty else [download(str(offset))],
                    "limit": 2,
                    "offset": offset,
                    "total": 4,
                },
            )
        if request.method == "DELETE":
            return httpx.Response(204)
        if request.url.path.endswith("/missing"):
            return httpx.Response(404, json={"message": "Not found"})
        if "/sessions/" in request.url.path:
            return httpx.Response(200, content=b"PK", headers={"Content-Type": "application/zip"})
        if request.headers["accept"] == "application/json":
            return httpx.Response(200, json=download("file-id"))
        return httpx.Response(
            200,
            stream=self.stream,
            headers={
                "Content-Type": self.content_type,
                "Content-Disposition": 'attachment; filename="file"',
            },
        )

    def client(self) -> Browserbase:
        return Browserbase(
            api_key="test-key",
            max_retries=0,
            http_client=httpx.Client(
                transport=httpx.MockTransport(self),
            ),
        )

    def async_client(self) -> AsyncBrowserbase:
        return AsyncBrowserbase(
            api_key="test-key",
            max_retries=0,
            http_client=httpx.AsyncClient(
                transport=httpx.MockTransport(self),
            ),
        )


def assert_pages(api: API, page: SyncOffsetPage[Download] | AsyncOffsetPage[Download], items: list[Download]) -> None:
    assert [item.id for item in items] == ["2", "3"]
    assert all(isinstance(item, Download) for item in items)
    assert (page.limit, page.offset, page.total) == (2, 2, 4)
    assert len(api.requests) == 2
    for index, request in enumerate(api.requests):
        assert dict(request.url.params) == {**WIRE_FILTERS, "offset": str(index + 2)}
        assert request.headers["x-bb-api-key"] == "test-key"


class TestDownloads:
    def test_pagination(self) -> None:
        api = API()
        with api.client() as client:
            page = client.downloads.list(**FILTERS)
            assert len(api.requests) == 1
            assert_pages(api, page, list(page))

    def test_empty_page(self) -> None:
        api = API(empty=True)
        with api.client() as client:
            assert list(client.downloads.list(session_id=SESSION_ID)) == []
        assert len(api.requests) == 1
        assert "limit" not in api.requests[0].url.params

    def test_metadata_delete_error_and_legacy_zip(self) -> None:
        api = API()
        with api.client() as client:
            assert isinstance(client.downloads.retrieve("file-id"), Download)
            assert api.requests[-1].headers["accept"] == "application/json"
            assert client.downloads.delete("file-id") is None
            with pytest.raises(NotFoundError):
                with client.downloads.with_streaming_response.download("missing"):
                    pytest.fail("404 must raise before yielding a stream")
            with client.sessions.downloads.with_streaming_response.list(SESSION_ID) as response:
                assert response.read() == b"PK"
            assert api.requests[-1].headers["accept"] == "application/zip"

    @pytest.mark.parametrize("content_type", ["application/octet-stream", "application/json"])
    @pytest.mark.parametrize("chunks", [(b"first", b"last"), ()])
    def test_stream_to_file_without_eager_reads(
        self, content_type: str, chunks: tuple[bytes, ...], tmp_path: Path
    ) -> None:
        stream = Chunks(chunks)
        api = API(stream=stream, content_type=content_type)
        with api.client() as client:
            manager = client.downloads.with_streaming_response.download("file-id")
            assert api.requests == []
            with manager as response:
                assert stream.reads == 0
                assert "application/json" not in api.requests[-1].headers["accept"]
                assert response.headers["content-type"] == content_type
                assert "attachment" in response.headers["content-disposition"]
                path = tmp_path / "file"
                response.stream_to_file(path, chunk_size=4)
                assert path.read_bytes() == b"".join(chunks)
            assert stream.closed

    def test_partial_read_and_stream_error_close_response(self) -> None:
        stream = Chunks()
        with API(stream=stream).client() as client:
            with client.downloads.with_streaming_response.download("file-id") as response:
                assert next(response.iter_bytes()) == b"first"
                assert stream.reads == 1
            assert stream.closed
        stream = Chunks(error=OSError("stream interrupted"))
        with API(stream=stream).client() as client:
            with pytest.raises(OSError, match="stream interrupted"):
                with client.downloads.with_streaming_response.download("file-id") as response:
                    list(response.iter_bytes())
            assert stream.closed


class TestAsyncDownloads:
    async def test_pagination(self) -> None:
        api = API()
        async with api.async_client() as client:
            page = await client.downloads.list(**FILTERS)
            assert len(api.requests) == 1
            assert_pages(api, page, [item async for item in page])

    async def test_empty_page(self) -> None:
        api = API(empty=True)
        async with api.async_client() as client:
            assert [item async for item in client.downloads.list(session_id=SESSION_ID)] == []
        assert len(api.requests) == 1

    async def test_metadata_delete_error_and_legacy_zip(self) -> None:
        api = API()
        async with api.async_client() as client:
            assert isinstance(await client.downloads.retrieve("file-id"), Download)
            assert api.requests[-1].headers["accept"] == "application/json"
            assert await client.downloads.delete("file-id") is None
            with pytest.raises(NotFoundError):
                async with client.downloads.with_streaming_response.download("missing"):
                    pytest.fail("404 must raise before yielding a stream")
            async with client.sessions.downloads.with_streaming_response.list(SESSION_ID) as response:
                assert await response.read() == b"PK"
            assert api.requests[-1].headers["accept"] == "application/zip"

    @pytest.mark.parametrize("content_type", ["application/octet-stream", "application/json"])
    @pytest.mark.parametrize("chunks", [(b"first", b"last"), ()])
    async def test_stream_to_file_without_eager_reads(
        self, content_type: str, chunks: tuple[bytes, ...], tmp_path: Path
    ) -> None:
        stream = Chunks(chunks)
        api = API(stream=stream, content_type=content_type)
        async with api.async_client() as client:
            manager = client.downloads.with_streaming_response.download("file-id")
            assert api.requests == []
            async with manager as response:
                assert stream.reads == 0
                assert "application/json" not in api.requests[-1].headers["accept"]
                assert response.headers["content-type"] == content_type
                path = tmp_path / "file"
                await response.stream_to_file(path, chunk_size=4)
                assert path.read_bytes() == b"".join(chunks)
            assert stream.closed

    async def test_cancellation_and_stream_error_close_response(self) -> None:
        for error in (asyncio.CancelledError(), OSError("stream interrupted")):
            stream = Chunks(error=error)
            async with API(stream=stream).async_client() as client:
                with pytest.raises(type(error)):
                    async with client.downloads.with_streaming_response.download("file-id") as response:
                        async for _ in response.iter_bytes():
                            pass
                assert stream.closed
