# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from browserbase.types.sessions import ReplayRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReplays:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Browserbase) -> None:
        replay = client.sessions.replays.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ReplayRetrieveResponse, replay, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Browserbase) -> None:
        response = client.sessions.replays.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replay = response.parse()
        assert_matches_type(ReplayRetrieveResponse, replay, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Browserbase) -> None:
        with client.sessions.replays.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replay = response.parse()
            assert_matches_type(ReplayRetrieveResponse, replay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.replays.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_page(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/replays/090").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        replay = client.sessions.replays.retrieve_page(
            page_id="090",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert replay.is_closed
        assert replay.json() == {"foo": "bar"}
        assert cast(Any, replay.is_closed) is True
        assert isinstance(replay, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_page(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/replays/090").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        replay = client.sessions.replays.with_raw_response.retrieve_page(
            page_id="090",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert replay.is_closed is True
        assert replay.http_request.headers.get("X-Stainless-Lang") == "python"
        assert replay.json() == {"foo": "bar"}
        assert isinstance(replay, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_page(self, client: Browserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/replays/090").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.sessions.replays.with_streaming_response.retrieve_page(
            page_id="090",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as replay:
            assert not replay.is_closed
            assert replay.http_request.headers.get("X-Stainless-Lang") == "python"

            assert replay.json() == {"foo": "bar"}
            assert cast(Any, replay.is_closed) is True
            assert isinstance(replay, StreamedBinaryAPIResponse)

        assert cast(Any, replay.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve_page(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.replays.with_raw_response.retrieve_page(
                page_id="090",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.sessions.replays.with_raw_response.retrieve_page(
                page_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncReplays:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrowserbase) -> None:
        replay = await async_client.sessions.replays.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ReplayRetrieveResponse, replay, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.sessions.replays.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replay = await response.parse()
        assert_matches_type(ReplayRetrieveResponse, replay, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.sessions.replays.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replay = await response.parse()
            assert_matches_type(ReplayRetrieveResponse, replay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.replays.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_page(self, async_client: AsyncBrowserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/replays/090").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        replay = await async_client.sessions.replays.retrieve_page(
            page_id="090",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert replay.is_closed
        assert await replay.json() == {"foo": "bar"}
        assert cast(Any, replay.is_closed) is True
        assert isinstance(replay, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_page(self, async_client: AsyncBrowserbase, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/replays/090").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        replay = await async_client.sessions.replays.with_raw_response.retrieve_page(
            page_id="090",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert replay.is_closed is True
        assert replay.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await replay.json() == {"foo": "bar"}
        assert isinstance(replay, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_page(
        self, async_client: AsyncBrowserbase, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/sessions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/replays/090").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.sessions.replays.with_streaming_response.retrieve_page(
            page_id="090",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as replay:
            assert not replay.is_closed
            assert replay.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await replay.json() == {"foo": "bar"}
            assert cast(Any, replay.is_closed) is True
            assert isinstance(replay, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, replay.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve_page(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.replays.with_raw_response.retrieve_page(
                page_id="090",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.sessions.replays.with_raw_response.retrieve_page(
                page_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
