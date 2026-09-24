# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase._utils import parse_datetime
from browserbase.types.functions import SecretListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Browserbase) -> None:
        secret = client.functions.secrets.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Browserbase) -> None:
        secret = client.functions.secrets.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            end_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Browserbase) -> None:
        response = client.functions.secrets.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Browserbase) -> None:
        with client.functions.secrets.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.functions.secrets.with_raw_response.list(
                id="",
            )

    @parametrize
    def test_method_attach(self, client: Browserbase) -> None:
        secret = client.functions.secrets.attach(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert secret is None

    @parametrize
    def test_raw_response_attach(self, client: Browserbase) -> None:
        response = client.functions.secrets.with_raw_response.attach(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @parametrize
    def test_streaming_response_attach(self, client: Browserbase) -> None:
        with client.functions.secrets.with_streaming_response.attach(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.functions.secrets.with_raw_response.attach(
                id="",
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_detach(self, client: Browserbase) -> None:
        secret = client.functions.secrets.detach(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert secret is None

    @parametrize
    def test_raw_response_detach(self, client: Browserbase) -> None:
        response = client.functions.secrets.with_raw_response.detach(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @parametrize
    def test_streaming_response_detach(self, client: Browserbase) -> None:
        with client.functions.secrets.with_streaming_response.detach(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_detach(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.functions.secrets.with_raw_response.detach(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.functions.secrets.with_raw_response.detach(
                secret_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserbase) -> None:
        secret = await async_client.functions.secrets.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        secret = await async_client.functions.secrets.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            end_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.functions.secrets.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.functions.secrets.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.functions.secrets.with_raw_response.list(
                id="",
            )

    @parametrize
    async def test_method_attach(self, async_client: AsyncBrowserbase) -> None:
        secret = await async_client.functions.secrets.attach(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert secret is None

    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.functions.secrets.with_raw_response.attach(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.functions.secrets.with_streaming_response.attach(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.functions.secrets.with_raw_response.attach(
                id="",
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_detach(self, async_client: AsyncBrowserbase) -> None:
        secret = await async_client.functions.secrets.detach(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert secret is None

    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.functions.secrets.with_raw_response.detach(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.functions.secrets.with_streaming_response.detach(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_detach(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.functions.secrets.with_raw_response.detach(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.functions.secrets.with_raw_response.detach(
                secret_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
