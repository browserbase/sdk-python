from __future__ import annotations

import pytest

from browserbase._utils import removeprefix, removesuffix


@pytest.mark.parametrize(
    ("string", "prefix"),
    [
        ("browserbase", "browser"),
        ("browserbase", "base"),
        ("browserbase", ""),
        ("", ""),
    ],
)
def test_removeprefix_matches_stdlib(string: str, prefix: str) -> None:
    assert removeprefix(string, prefix) == string.removeprefix(prefix)


@pytest.mark.parametrize(
    ("string", "suffix"),
    [
        ("browserbase", "base"),
        ("browserbase", "browser"),
        ("browserbase", ""),
        ("", ""),
    ],
)
def test_removesuffix_matches_stdlib(string: str, suffix: str) -> None:
    assert removesuffix(string, suffix) == string.removesuffix(suffix)
