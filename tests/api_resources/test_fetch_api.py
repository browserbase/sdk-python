# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase.types import FetchAPICreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFetchAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Browserbase) -> None:
        fetch_api = client.fetch_api.create(
            url="https://example.com",
        )
        assert_matches_type(FetchAPICreateResponse, fetch_api, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Browserbase) -> None:
        fetch_api = client.fetch_api.create(
            url="https://example.com",
            allow_insecure_ssl=True,
            allow_redirects=True,
            proxies=True,
        )
        assert_matches_type(FetchAPICreateResponse, fetch_api, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Browserbase) -> None:
        response = client.fetch_api.with_raw_response.create(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch_api = response.parse()
        assert_matches_type(FetchAPICreateResponse, fetch_api, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Browserbase) -> None:
        with client.fetch_api.with_streaming_response.create(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch_api = response.parse()
            assert_matches_type(FetchAPICreateResponse, fetch_api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFetchAPI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBrowserbase) -> None:
        fetch_api = await async_client.fetch_api.create(
            url="https://example.com",
        )
        assert_matches_type(FetchAPICreateResponse, fetch_api, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        fetch_api = await async_client.fetch_api.create(
            url="https://example.com",
            allow_insecure_ssl=True,
            allow_redirects=True,
            proxies=True,
        )
        assert_matches_type(FetchAPICreateResponse, fetch_api, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.fetch_api.with_raw_response.create(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch_api = await response.parse()
        assert_matches_type(FetchAPICreateResponse, fetch_api, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.fetch_api.with_streaming_response.create(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch_api = await response.parse()
            assert_matches_type(FetchAPICreateResponse, fetch_api, path=["response"])

        assert cast(Any, response.is_closed) is True
