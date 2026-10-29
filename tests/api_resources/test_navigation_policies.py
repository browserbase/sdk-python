# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase.types import (
    NavigationPolicy,
    NavigationPolicyListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNavigationPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Browserbase) -> None:
        navigation_policy = client.navigation_policies.create(
            name="x",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Browserbase) -> None:
        navigation_policy = client.navigation_policies.create(
            name="x",
            allowed_categories=["adult"],
            blocked_categories=["adult"],
            default_decision="allow",
            description="description",
            domain_overrides=[
                {
                    "decision": "allow",
                    "domain": "x",
                }
            ],
            enabled=True,
            unknown_domain_behavior="allow",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Browserbase) -> None:
        response = client.navigation_policies.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = response.parse()
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Browserbase) -> None:
        with client.navigation_policies.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = response.parse()
            assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Browserbase) -> None:
        navigation_policy = client.navigation_policies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Browserbase) -> None:
        response = client.navigation_policies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = response.parse()
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Browserbase) -> None:
        with client.navigation_policies.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = response.parse()
            assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.navigation_policies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Browserbase) -> None:
        navigation_policy = client.navigation_policies.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Browserbase) -> None:
        navigation_policy = client.navigation_policies.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_categories=["adult"],
            blocked_categories=["adult"],
            default_decision="allow",
            description="description",
            domain_overrides=[
                {
                    "decision": "allow",
                    "domain": "x",
                }
            ],
            enabled=True,
            name="x",
            unknown_domain_behavior="allow",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Browserbase) -> None:
        response = client.navigation_policies.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = response.parse()
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Browserbase) -> None:
        with client.navigation_policies.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = response.parse()
            assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.navigation_policies.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Browserbase) -> None:
        navigation_policy = client.navigation_policies.list()
        assert_matches_type(NavigationPolicyListResponse, navigation_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Browserbase) -> None:
        response = client.navigation_policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = response.parse()
        assert_matches_type(NavigationPolicyListResponse, navigation_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Browserbase) -> None:
        with client.navigation_policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = response.parse()
            assert_matches_type(NavigationPolicyListResponse, navigation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Browserbase) -> None:
        navigation_policy = client.navigation_policies.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert navigation_policy is None

    @parametrize
    def test_raw_response_delete(self, client: Browserbase) -> None:
        response = client.navigation_policies.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = response.parse()
        assert navigation_policy is None

    @parametrize
    def test_streaming_response_delete(self, client: Browserbase) -> None:
        with client.navigation_policies.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = response.parse()
            assert navigation_policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.navigation_policies.with_raw_response.delete(
                "",
            )


class TestAsyncNavigationPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBrowserbase) -> None:
        navigation_policy = await async_client.navigation_policies.create(
            name="x",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        navigation_policy = await async_client.navigation_policies.create(
            name="x",
            allowed_categories=["adult"],
            blocked_categories=["adult"],
            default_decision="allow",
            description="description",
            domain_overrides=[
                {
                    "decision": "allow",
                    "domain": "x",
                }
            ],
            enabled=True,
            unknown_domain_behavior="allow",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.navigation_policies.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = await response.parse()
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.navigation_policies.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = await response.parse()
            assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrowserbase) -> None:
        navigation_policy = await async_client.navigation_policies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.navigation_policies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = await response.parse()
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.navigation_policies.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = await response.parse()
            assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.navigation_policies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBrowserbase) -> None:
        navigation_policy = await async_client.navigation_policies.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        navigation_policy = await async_client.navigation_policies.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_categories=["adult"],
            blocked_categories=["adult"],
            default_decision="allow",
            description="description",
            domain_overrides=[
                {
                    "decision": "allow",
                    "domain": "x",
                }
            ],
            enabled=True,
            name="x",
            unknown_domain_behavior="allow",
        )
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.navigation_policies.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = await response.parse()
        assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.navigation_policies.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = await response.parse()
            assert_matches_type(NavigationPolicy, navigation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.navigation_policies.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserbase) -> None:
        navigation_policy = await async_client.navigation_policies.list()
        assert_matches_type(NavigationPolicyListResponse, navigation_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.navigation_policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = await response.parse()
        assert_matches_type(NavigationPolicyListResponse, navigation_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.navigation_policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = await response.parse()
            assert_matches_type(NavigationPolicyListResponse, navigation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBrowserbase) -> None:
        navigation_policy = await async_client.navigation_policies.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert navigation_policy is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.navigation_policies.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigation_policy = await response.parse()
        assert navigation_policy is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.navigation_policies.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigation_policy = await response.parse()
            assert navigation_policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.navigation_policies.with_raw_response.delete(
                "",
            )
