# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase.types import (
    AgentListResponse,
    AgentCreateResponse,
    AgentUpdateResponse,
    AgentRetrieveResponse,
)
from browserbase._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Browserbase) -> None:
        agent = client.agents.create(
            name="x",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Browserbase) -> None:
        agent = client.agents.create(
            name="x",
            result_schema={"foo": "bar"},
            system_prompt="x",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Browserbase) -> None:
        response = client.agents.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Browserbase) -> None:
        with client.agents.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Browserbase) -> None:
        agent = client.agents.retrieve(
            "agentId",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Browserbase) -> None:
        response = client.agents.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Browserbase) -> None:
        with client.agents.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Browserbase) -> None:
        agent = client.agents.update(
            agent_id="agentId",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Browserbase) -> None:
        agent = client.agents.update(
            agent_id="agentId",
            name="x",
            result_schema={"foo": "bar"},
            system_prompt="x",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Browserbase) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Browserbase) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    def test_method_list(self, client: Browserbase) -> None:
        agent = client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Browserbase) -> None:
        agent = client.agents.list(
            cursor="cursor",
            end_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Browserbase) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Browserbase) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Browserbase) -> None:
        agent = client.agents.delete(
            "agentId",
        )
        assert agent is None

    @parametrize
    def test_raw_response_delete(self, client: Browserbase) -> None:
        response = client.agents.with_raw_response.delete(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @parametrize
    def test_streaming_response_delete(self, client: Browserbase) -> None:
        with client.agents.with_streaming_response.delete(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBrowserbase) -> None:
        agent = await async_client.agents.create(
            name="x",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        agent = await async_client.agents.create(
            name="x",
            result_schema={"foo": "bar"},
            system_prompt="x",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrowserbase) -> None:
        agent = await async_client.agents.retrieve(
            "agentId",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBrowserbase) -> None:
        agent = await async_client.agents.update(
            agent_id="agentId",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        agent = await async_client.agents.update(
            agent_id="agentId",
            name="x",
            result_schema={"foo": "bar"},
            system_prompt="x",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserbase) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        agent = await async_client.agents.list(
            cursor="cursor",
            end_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBrowserbase) -> None:
        agent = await async_client.agents.delete(
            "agentId",
        )
        assert agent is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )
