# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase._utils import parse_datetime
from browserbase.types.agents import (
    RunListResponse,
    RunCreateResponse,
    RunRetrieveResponse,
    RunListMessagesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Browserbase) -> None:
        run = client.agents.runs.create(
            task="x",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Browserbase) -> None:
        run = client.agents.runs.create(
            task="x",
            agent_id="agentId",
            browser_settings={
                "context": {
                    "id": "id",
                    "persist": True,
                },
                "proxies": True,
                "verified": True,
            },
            result_schema={"foo": "bar"},
            variables={
                "foo": {
                    "value": "value",
                    "description": "description",
                }
            },
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Browserbase) -> None:
        response = client.agents.runs.with_raw_response.create(
            task="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Browserbase) -> None:
        with client.agents.runs.with_streaming_response.create(
            task="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Browserbase) -> None:
        run = client.agents.runs.retrieve(
            "runId",
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Browserbase) -> None:
        response = client.agents.runs.with_raw_response.retrieve(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Browserbase) -> None:
        with client.agents.runs.with_streaming_response.retrieve(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agents.runs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Browserbase) -> None:
        run = client.agents.runs.list()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Browserbase) -> None:
        run = client.agents.runs.list(
            agent_id="agentId",
            cursor="cursor",
            end_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="PENDING",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Browserbase) -> None:
        response = client.agents.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Browserbase) -> None:
        with client.agents.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_messages(self, client: Browserbase) -> None:
        run = client.agents.runs.list_messages(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @parametrize
    def test_method_list_messages_with_all_params(self, client: Browserbase) -> None:
        run = client.agents.runs.list_messages(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            all=True,
            limit=1,
            since="since",
        )
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @parametrize
    def test_raw_response_list_messages(self, client: Browserbase) -> None:
        response = client.agents.runs.with_raw_response.list_messages(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_list_messages(self, client: Browserbase) -> None:
        with client.agents.runs.with_streaming_response.list_messages(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListMessagesResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_messages(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agents.runs.with_raw_response.list_messages(
                run_id="",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBrowserbase) -> None:
        run = await async_client.agents.runs.create(
            task="x",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        run = await async_client.agents.runs.create(
            task="x",
            agent_id="agentId",
            browser_settings={
                "context": {
                    "id": "id",
                    "persist": True,
                },
                "proxies": True,
                "verified": True,
            },
            result_schema={"foo": "bar"},
            variables={
                "foo": {
                    "value": "value",
                    "description": "description",
                }
            },
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.runs.with_raw_response.create(
            task="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.runs.with_streaming_response.create(
            task="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrowserbase) -> None:
        run = await async_client.agents.runs.retrieve(
            "runId",
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.runs.with_raw_response.retrieve(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.runs.with_streaming_response.retrieve(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agents.runs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserbase) -> None:
        run = await async_client.agents.runs.list()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        run = await async_client.agents.runs.list(
            agent_id="agentId",
            cursor="cursor",
            end_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="PENDING",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_messages(self, async_client: AsyncBrowserbase) -> None:
        run = await async_client.agents.runs.list_messages(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @parametrize
    async def test_method_list_messages_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        run = await async_client.agents.runs.list_messages(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            all=True,
            limit=1,
            since="since",
        )
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.runs.with_raw_response.list_messages(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.runs.with_streaming_response.list_messages(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListMessagesResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agents.runs.with_raw_response.list_messages(
                run_id="",
            )
