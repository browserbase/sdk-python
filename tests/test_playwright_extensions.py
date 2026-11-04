from __future__ import annotations

import importlib
from types import ModuleType

import httpx
import pytest

from browserbase import APIStatusError


@pytest.fixture
def extension_example(monkeypatch: pytest.MonkeyPatch) -> ModuleType:
    monkeypatch.setenv("BROWSERBASE_API_KEY", "test-api-key")
    monkeypatch.setenv("BROWSERBASE_PROJECT_ID", "test-project-id")
    return importlib.import_module("examples.playwright_extensions")


def test_expect_api_status_error_accepts_api_failure(
    extension_example: ModuleType, capsys: pytest.CaptureFixture[str]
) -> None:
    request = httpx.Request("GET", "https://example.com/extensions/id")
    response = httpx.Response(404, request=request)

    def operation() -> object:
        raise APIStatusError("not found", response=response, body=None)

    extension_example.expect_api_status_error(
        operation,
        failure_message="operation unexpectedly succeeded",
        success_message="operation failed as expected",
    )

    assert "operation failed as expected" in capsys.readouterr().out


def test_expect_api_status_error_rejects_unexpected_success(extension_example: ModuleType) -> None:
    with pytest.raises(AssertionError, match="operation unexpectedly succeeded"):
        extension_example.expect_api_status_error(
            lambda: object(),
            failure_message="operation unexpectedly succeeded",
            success_message="operation failed as expected",
        )


def test_expect_api_status_error_does_not_hide_other_errors(extension_example: ModuleType) -> None:
    def operation() -> object:
        raise RuntimeError("unexpected failure")

    with pytest.raises(RuntimeError, match="unexpected failure"):
        extension_example.expect_api_status_error(
            operation,
            failure_message="operation unexpectedly succeeded",
            success_message="operation failed as expected",
        )
