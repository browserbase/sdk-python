# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from browserbase import Browserbase, AsyncBrowserbase
from tests.utils import assert_matches_type
from browserbase.types import (
    SessionListResponse,
    SessionDebugResponse,
    SessionCreateResponse,
    SessionUpdateResponse,
    SessionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Browserbase) -> None:
        session = client.sessions.create(
            project_id="projectId",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Browserbase) -> None:
        session = client.sessions.create(
            project_id="projectId",
            browser_settings={
                "advanced_stealth": True,
                "block_ads": True,
                "captcha_image_selector": "captchaImageSelector",
                "captcha_input_selector": "captchaInputSelector",
                "context": {
                    "id": "id",
                    "persist": True,
                },
                "extension_id": "extensionId",
                "fingerprint": {
                    "browsers": ["chrome"],
                    "devices": ["desktop"],
                    "http_version": "1",
                    "locales": ["string"],
                    "operating_systems": ["android"],
                    "screen": {
                        "max_height": 0,
                        "max_width": 0,
                        "min_height": 0,
                        "min_width": 0,
                    },
                },
                "log_session": True,
                "record_session": True,
                "solve_captchas": True,
                "viewport": {
                    "height": 0,
                    "width": 0,
                },
            },
            extension_id="extensionId",
            keep_alive=True,
            proxies=[
                {
                    "type": "browserbase",
                    "domain_pattern": "domainPattern",
                    "geolocation": {
                        "country": "xx",
                        "city": "city",
                        "state": "xx",
                    },
                }
            ],
            region="us-west-2",
            api_timeout=60,
            user_metadata={"foo": "bar"},
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Browserbase) -> None:
        response = client.sessions.with_raw_response.create(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Browserbase) -> None:
        with client.sessions.with_streaming_response.create(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Browserbase) -> None:
        session = client.sessions.retrieve(
            "id",
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Browserbase) -> None:
        response = client.sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Browserbase) -> None:
        with client.sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionRetrieveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Browserbase) -> None:
        session = client.sessions.update(
            id="id",
            project_id="projectId",
            status="REQUEST_RELEASE",
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Browserbase) -> None:
        response = client.sessions.with_raw_response.update(
            id="id",
            project_id="projectId",
            status="REQUEST_RELEASE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Browserbase) -> None:
        with client.sessions.with_streaming_response.update(
            id="id",
            project_id="projectId",
            status="REQUEST_RELEASE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionUpdateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.with_raw_response.update(
                id="",
                project_id="projectId",
                status="REQUEST_RELEASE",
            )

    @parametrize
    def test_method_list(self, client: Browserbase) -> None:
        session = client.sessions.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Browserbase) -> None:
        session = client.sessions.list(
            q="q",
            status="RUNNING",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Browserbase) -> None:
        response = client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Browserbase) -> None:
        with client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_debug(self, client: Browserbase) -> None:
        session = client.sessions.debug(
            "id",
        )
        assert_matches_type(SessionDebugResponse, session, path=["response"])

    @parametrize
    def test_raw_response_debug(self, client: Browserbase) -> None:
        response = client.sessions.with_raw_response.debug(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDebugResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_debug(self, client: Browserbase) -> None:
        with client.sessions.with_streaming_response.debug(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionDebugResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_debug(self, client: Browserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.with_raw_response.debug(
                "",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBrowserbase) -> None:
        session = await async_client.sessions.create(
            project_id="projectId",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        session = await async_client.sessions.create(
            project_id="projectId",
            browser_settings={
                "advanced_stealth": True,
                "block_ads": True,
                "captcha_image_selector": "captchaImageSelector",
                "captcha_input_selector": "captchaInputSelector",
                "context": {
                    "id": "id",
                    "persist": True,
                },
                "extension_id": "extensionId",
                "fingerprint": {
                    "browsers": ["chrome"],
                    "devices": ["desktop"],
                    "http_version": "1",
                    "locales": ["string"],
                    "operating_systems": ["android"],
                    "screen": {
                        "max_height": 0,
                        "max_width": 0,
                        "min_height": 0,
                        "min_width": 0,
                    },
                },
                "log_session": True,
                "record_session": True,
                "solve_captchas": True,
                "viewport": {
                    "height": 0,
                    "width": 0,
                },
            },
            extension_id="extensionId",
            keep_alive=True,
            proxies=[
                {
                    "type": "browserbase",
                    "domain_pattern": "domainPattern",
                    "geolocation": {
                        "country": "xx",
                        "city": "city",
                        "state": "xx",
                    },
                }
            ],
            region="us-west-2",
            api_timeout=60,
            user_metadata={"foo": "bar"},
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.sessions.with_raw_response.create(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.sessions.with_streaming_response.create(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrowserbase) -> None:
        session = await async_client.sessions.retrieve(
            "id",
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionRetrieveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBrowserbase) -> None:
        session = await async_client.sessions.update(
            id="id",
            project_id="projectId",
            status="REQUEST_RELEASE",
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.sessions.with_raw_response.update(
            id="id",
            project_id="projectId",
            status="REQUEST_RELEASE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.sessions.with_streaming_response.update(
            id="id",
            project_id="projectId",
            status="REQUEST_RELEASE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionUpdateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.with_raw_response.update(
                id="",
                project_id="projectId",
                status="REQUEST_RELEASE",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserbase) -> None:
        session = await async_client.sessions.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserbase) -> None:
        session = await async_client.sessions.list(
            q="q",
            status="RUNNING",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_debug(self, async_client: AsyncBrowserbase) -> None:
        session = await async_client.sessions.debug(
            "id",
        )
        assert_matches_type(SessionDebugResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_debug(self, async_client: AsyncBrowserbase) -> None:
        response = await async_client.sessions.with_raw_response.debug(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDebugResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_debug(self, async_client: AsyncBrowserbase) -> None:
        async with async_client.sessions.with_streaming_response.debug(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionDebugResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_debug(self, async_client: AsyncBrowserbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.with_raw_response.debug(
                "",
            )
