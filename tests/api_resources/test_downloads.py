# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase.types import Download
from browserbase._utils import parse_datetime
from browserbase._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from browserbase.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Browserbase) -> None:
        download = client.downloads.retrieve(
            "id",
        )
        assert_matches_type(Download, download, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Browserbase) -> None:
        response = client.downloads.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(Download, download, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Browserbase) -> None:
        with client.downloads.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(Download, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.downloads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Browserbase) -> None:
        download = client.downloads.list(
            session_id="sessionId",
        )
        assert_matches_type(SyncOffsetPage[Download], download, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Browserbase) -> None:
        download = client.downloads.list(
            session_id="sessionId",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename="filename",
            limit=1,
            max_size=0,
            mime_type="mimeType",
            min_size=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[Download], download, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Browserbase) -> None:
        response = client.downloads.with_raw_response.list(
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(SyncOffsetPage[Download], download, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Browserbase) -> None:
        with client.downloads.with_streaming_response.list(
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(SyncOffsetPage[Download], download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Browserbase) -> None:
        download = client.downloads.delete(
            "id",
        )
        assert download is None

    @parametrize
    def test_raw_response_delete(self, client: Browserbase) -> None:
        response = client.downloads.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert download is None

    @parametrize
    def test_streaming_response_delete(self, client: Browserbase) -> None:
        with client.downloads.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert download is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.downloads.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/downloads/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        download = client.downloads.download(
            "id",
        )
        assert download.is_closed
        assert download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/downloads/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        download = client.downloads.with_raw_response.download(
            "id",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert download.json() == {"foo": "bar"}
        assert isinstance(download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/downloads/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.downloads.with_streaming_response.download(
            "id",
        ) as download:
            assert not download.is_closed
            assert download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert download.json() == {"foo": "bar"}
            assert cast(Any, download.is_closed) is True
            assert isinstance(download, StreamedBinaryAPIResponse)

        assert cast(Any, download.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.downloads.with_raw_response.download(
                "",
            )


class TestAsyncDownloads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrowserbase) -> None:
        download = await async_client.downloads.retrieve(
            "id",
        )
        assert_matches_type(Download, download, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.downloads.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(Download, download, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.downloads.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(Download, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.downloads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserbase) -> None:
        download = await async_client.downloads.list(
            session_id="sessionId",
        )
        assert_matches_type(AsyncOffsetPage[Download], download, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        download = await async_client.downloads.list(
            session_id="sessionId",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename="filename",
            limit=1,
            max_size=0,
            mime_type="mimeType",
            min_size=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[Download], download, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.downloads.with_raw_response.list(
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(AsyncOffsetPage[Download], download, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.downloads.with_streaming_response.list(
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(AsyncOffsetPage[Download], download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBrowserbase) -> None:
        download = await async_client.downloads.delete(
            "id",
        )
        assert download is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.downloads.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert download is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.downloads.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert download is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.downloads.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncBrowserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/downloads/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        download = await async_client.downloads.download(
            "id",
        )
        assert download.is_closed
        assert await download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncBrowserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/downloads/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        download = await async_client.downloads.with_raw_response.download(
            "id",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await download.json() == {"foo": "bar"}
        assert isinstance(download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncBrowserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/downloads/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.downloads.with_streaming_response.download(
            "id",
        ) as download:
            assert not download.is_closed
            assert download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await download.json() == {"foo": "bar"}
            assert cast(Any, download.is_closed) is True
            assert isinstance(download, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, download.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.downloads.with_raw_response.download(
                "",
            )
