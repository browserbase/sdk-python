from __future__ import annotations

import re
from pathlib import Path

README = Path(__file__).parent.parent / "README.md"


def python_blocks() -> list[str]:
    return re.findall(r"```(?:py|python)\n(.*?)```", README.read_text(encoding="utf-8"), flags=re.DOTALL)


def test_quickstart_is_a_complete_python_block() -> None:
    quickstart = next(block for block in python_blocks() if "sync_playwright" in block)

    assert "def run(playwright: Playwright) -> None:" in quickstart
    assert 'if __name__ == "__main__":' in quickstart
    compile(quickstart, str(README), "exec")


def test_timeout_example_imports_httpx() -> None:
    timeout_example = next(block for block in python_blocks() if "httpx.Timeout" in block)

    assert "import httpx" in timeout_example
    compile(timeout_example, str(README), "exec")
