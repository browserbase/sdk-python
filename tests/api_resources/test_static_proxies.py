# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase.types import StaticProxyListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStaticProxies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Browserbase) -> None:
        static_proxy = client.static_proxies.list()
        assert_matches_type(StaticProxyListResponse, static_proxy, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Browserbase) -> None:
        static_proxy = client.static_proxies.list(
            cursor="x",
            limit=1,
        )
        assert_matches_type(StaticProxyListResponse, static_proxy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Browserbase) -> None:
        response = client.static_proxies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        static_proxy = response.parse()
        assert_matches_type(StaticProxyListResponse, static_proxy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Browserbase) -> None:
        with client.static_proxies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            static_proxy = response.parse()
            assert_matches_type(StaticProxyListResponse, static_proxy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStaticProxies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserbase) -> None:
        static_proxy = await async_client.static_proxies.list()
        assert_matches_type(StaticProxyListResponse, static_proxy, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        static_proxy = await async_client.static_proxies.list(
            cursor="x",
            limit=1,
        )
        assert_matches_type(StaticProxyListResponse, static_proxy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.static_proxies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        static_proxy = await response.parse()
        assert_matches_type(StaticProxyListResponse, static_proxy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.static_proxies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            static_proxy = await response.parse()
            assert_matches_type(StaticProxyListResponse, static_proxy, path=["response"])

        assert cast(Any, response.is_closed) is True
