import os
from typing import Generator

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright

from browserbase import Browserbase

from .. import (
    BROWSERBASE_API_KEY,
    playwright_basic,
    playwright_proxy,
    playwright_captcha,
    playwright_contexts,
    playwright_downloads,
)

bb = Browserbase(api_key=BROWSERBASE_API_KEY)
load_dotenv()

CI = os.getenv("CI", "false").lower() == "true"


@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    with sync_playwright() as p:
        yield p


def test_playwright_basic(playwright: Playwright) -> None:
    playwright_basic.run(playwright)


@pytest.mark.skipif(CI, reason="Flaky and fails on CI")
def test_playwright_captcha(playwright: Playwright) -> None:
    playwright_captcha.run(playwright)


def test_playwright_contexts(playwright: Playwright) -> None:
    playwright_contexts.run(playwright)


def test_playwright_downloads(playwright: Playwright) -> None:
    playwright_downloads.run(playwright)


def test_playwright_proxy_enable_via_create_session(playwright: Playwright) -> None:
    playwright_proxy.run_enable_via_create_session(playwright)


def test_playwright_proxy_enable_via_querystring(playwright: Playwright) -> None:
    playwright_proxy.run_enable_via_querystring_with_created_session(playwright)


@pytest.mark.skipif(CI, reason="Flaky and fails on CI")
def test_playwright_proxy_geolocation_country(playwright: Playwright) -> None:
    playwright_proxy.run_geolocation_country(playwright)


@pytest.mark.skipif(CI, reason="Flaky and fails on CI")
def test_playwright_proxy_geolocation_state(playwright: Playwright) -> None:
    playwright_proxy.run_geolocation_state(playwright)


@pytest.mark.skipif(CI, reason="Flaky and fails on CI")
def test_playwright_proxy_geolocation_american_city(playwright: Playwright) -> None:
    playwright_proxy.run_geolocation_american_city(playwright)


@pytest.mark.skipif(CI, reason="Flaky and fails on CI")
def test_playwright_proxy_geolocation_non_american_city(playwright: Playwright) -> None:
    playwright_proxy.run_geolocation_non_american_city(playwright)
