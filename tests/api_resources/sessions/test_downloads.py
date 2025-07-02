# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from browserbase import Browserbase, AsyncBrowserbase
from browserbase._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/downloads").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        download = client.sessions.downloads.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert download.is_closed
        assert download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/downloads").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        download = client.sessions.downloads.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert download.json() == {"foo": "bar"}
        assert isinstance(download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/downloads").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.sessions.downloads.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as download:
            assert not download.is_closed
            assert download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert download.json() == {"foo": "bar"}
            assert cast(Any, download.is_closed) is True
            assert isinstance(download, StreamedBinaryAPIResponse)

        assert cast(Any, download.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.downloads.with_raw_response.list(
                "",
            )


class TestAsyncDownloads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncBrowserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/downloads").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        download = await async_client.sessions.downloads.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert download.is_closed
        assert await download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncBrowserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/downloads").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        download = await async_client.sessions.downloads.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await download.json() == {"foo": "bar"}
        assert isinstance(download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/downloads").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.sessions.downloads.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as download:
            assert not download.is_closed
            assert download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await download.json() == {"foo": "bar"}
            assert cast(Any, download.is_closed) is True
            assert isinstance(download, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, download.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.downloads.with_raw_response.list(
                "",
            )
