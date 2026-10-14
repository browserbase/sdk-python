# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase.types import SearchWebResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_web_overload_1(self, client: Browserbase) -> None:
        search = client.search.web(
            provider="parallel",
        )
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    def test_method_web_with_all_params_overload_1(self, client: Browserbase) -> None:
        search = client.search.web(
            provider="parallel",
            mode="fast",
            num_results=1,
            query="x",
        )
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    def test_raw_response_web_overload_1(self, client: Browserbase) -> None:
        response = client.search.with_raw_response.web(
            provider="parallel",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_web_overload_1(self, client: Browserbase) -> None:
        with client.search.with_streaming_response.web(
            provider="parallel",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchWebResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_web_overload_2(self, client: Browserbase) -> None:
        search = client.search.web()
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    def test_method_web_with_all_params_overload_2(self, client: Browserbase) -> None:
        search = client.search.web(
            mode="fast",
            num_results=1,
            provider="exa",
            query="x",
        )
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    def test_raw_response_web_overload_2(self, client: Browserbase) -> None:
        response = client.search.with_raw_response.web()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_web_overload_2(self, client: Browserbase) -> None:
        with client.search.with_streaming_response.web() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchWebResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_web_overload_1(self, async_client: AsyncBrowserbase) -> None:
        search = await async_client.search.web(
            provider="parallel",
        )
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    async def test_method_web_with_all_params_overload_1(self, async_client: AsyncBrowserbase) -> None:
        search = await async_client.search.web(
            provider="parallel",
            mode="fast",
            num_results=1,
            query="x",
        )
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_web_overload_1(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.search.with_raw_response.web(
            provider="parallel",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_web_overload_1(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.search.with_streaming_response.web(
            provider="parallel",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchWebResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_web_overload_2(self, async_client: AsyncBrowserbase) -> None:
        search = await async_client.search.web()
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    async def test_method_web_with_all_params_overload_2(self, async_client: AsyncBrowserbase) -> None:
        search = await async_client.search.web(
            mode="fast",
            num_results=1,
            provider="exa",
            query="x",
        )
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_web_overload_2(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.search.with_raw_response.web()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchWebResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_web_overload_2(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.search.with_streaming_response.web() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchWebResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
