import re
from pathlib import Path


def test_readme_code_fences_are_balanced() -> None:
    fences = re.findall(r"^```(.*)$", (Path(__file__).parent.parent / "README.md").read_text(), re.M)
    assert fences[1::2] == [""] * (len(fences) // 2) and all(fences[::2])
