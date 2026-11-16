import pytest

from browserbase._utils import removeprefix, removesuffix


@pytest.mark.parametrize("affix", ["", "a", "c", "abc", "abcd"])
def test_matches_stdlib(affix: str) -> None:
    assert removeprefix("abc", affix) == "abc".removeprefix(affix)
    assert removesuffix("abc", affix) == "abc".removesuffix(affix)
