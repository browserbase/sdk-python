# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase.types import Label, LabelListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Browserbase) -> None:
        label = client.labels.create(
            name="name",
        )
        assert_matches_type(Label, label, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Browserbase) -> None:
        response = client.labels.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(Label, label, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Browserbase) -> None:
        with client.labels.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(Label, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Browserbase) -> None:
        label = client.labels.update(
            label_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Label, label, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Browserbase) -> None:
        response = client.labels.with_raw_response.update(
            label_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(Label, label, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Browserbase) -> None:
        with client.labels.with_streaming_response.update(
            label_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(Label, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `label_id` but received ''"):
            client.labels.with_raw_response.update(
                label_id="",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Browserbase) -> None:
        label = client.labels.list()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Browserbase) -> None:
        label = client.labels.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Browserbase) -> None:
        response = client.labels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Browserbase) -> None:
        with client.labels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelListResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Browserbase) -> None:
        label = client.labels.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert label is None

    @parametrize
    def test_raw_response_delete(self, client: Browserbase) -> None:
        response = client.labels.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert label is None

    @parametrize
    def test_streaming_response_delete(self, client: Browserbase) -> None:
        with client.labels.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `label_id` but received ''"):
            client.labels.with_raw_response.delete(
                "",
            )


class TestAsyncLabels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBrowserbase) -> None:
        label = await async_client.labels.create(
            name="name",
        )
        assert_matches_type(Label, label, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.labels.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(Label, label, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.labels.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(Label, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncBrowserbase) -> None:
        label = await async_client.labels.update(
            label_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Label, label, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.labels.with_raw_response.update(
            label_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(Label, label, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.labels.with_streaming_response.update(
            label_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(Label, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `label_id` but received ''"):
            await async_client.labels.with_raw_response.update(
                label_id="",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserbase) -> None:
        label = await async_client.labels.list()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        label = await async_client.labels.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.labels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.labels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelListResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBrowserbase) -> None:
        label = await async_client.labels.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert label is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.labels.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert label is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.labels.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `label_id` but received ''"):
            await async_client.labels.with_raw_response.delete(
                "",
            )
