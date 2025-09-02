from typing import Union

import pytest

from mdfy import MdHeader


@pytest.mark.parametrize(
    "input_text, level, expected_output",
    [
        ("Header", 1, "# Header"),
        ("Sub Header", 2, "## Sub Header"),
        ("Deeper Header", 3, "### Deeper Header"),
        ("No Level Specified", None, "# No Level Specified"),
    ],
)
def test_mdheader_formatting(
    input_text: str, level: Union[int, None], expected_output: str
) -> None:
    if level:
        header = MdHeader(input_text, level)
    else:
        header = MdHeader(input_text)
    assert str(header) == expected_output


def test_mdheader_invalid_level_warning() -> None:
    with pytest.warns(UserWarning, match="Header level 10 is out of range. Setting to 1."):
        header = MdHeader("Invalid Level Header", level=10)
    assert str(header) == "# Invalid Level Header"


def test_mdheader_indent() -> None:
    header = MdHeader("Indented Header", level=2, indent="  ")
    assert str(header) == "  ## Indented Header"
