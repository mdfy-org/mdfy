from typing import Union
import pytest
from unittest.mock import patch

from mdfy.elements.seheader import MdSeHeader


@pytest.mark.parametrize(
    "content, level, expected_output",
    [
        ("Header", 1, "Header\n===\n"),
        ("Sub Header", 2, "Sub Header\n---\n"),
        ("Multi\nLine\nHeader", 1, "Multi\nLine\nHeader\n===\n"),
        ("Multi\nLine\nHeader", 2, "Multi\nLine\nHeader\n---\n"),
    ],
    ids=["level1", "level2", "multiline_level1", "multiline_level2"],
)
def test_mdseheader_basic_formatting(
    content: str, level: int, expected_output: str
) -> None:
    header = MdSeHeader(content, level)
    assert str(header) == expected_output


@pytest.mark.parametrize(
    "content, indent, level, expected_output",
    [
        ("Header", 0, 1, "Header\n===\n"),
        ("Header", 1, 1, "Header\n ===\n"),
        ("Header", 2, 1, "Header\n  ===\n"),
        ("Header", 3, 1, "Header\n   ===\n"),
        ("Header", 0, 2, "Header\n---\n"),
        ("Header", 1, 2, "Header\n ---\n"),
        ("Header", 2, 2, "Header\n  ---\n"),
        ("Header", 3, 2, "Header\n   ---\n"),
    ],
    ids=[
        "indent0_level1",
        "indent1_level1",
        "indent2_level1",
        "indent3_level1",
        "indent0_level2",
        "indent1_level2",
        "indent2_level2",
        "indent3_level2",
    ],
)
def test_mdseheader_with_indent(
    content: str, indent: int, level: int, expected_output: str
) -> None:
    header = MdSeHeader(content, level, indent)
    assert str(header) == expected_output


@pytest.mark.parametrize(
    "content, underline_length, level, expected_output",
    [
        ("Header", 3, 1, "Header\n===\n"),
        ("Header", 5, 1, "Header\n=====\n"),
        ("Header", 10, 1, "Header\n==========\n"),
        ("Header", 3, 2, "Header\n---\n"),
        ("Header", 5, 2, "Header\n-----\n"),
        ("Header", 10, 2, "Header\n----------\n"),
    ],
    ids=[
        "length3_level1",
        "length5_level1",
        "length10_level1",
        "length3_level2",
        "length5_level2",
        "length10_level2",
    ],
)
def test_mdseheader_with_underline_length(
    content: str, underline_length: int, level: int, expected_output: str
) -> None:
    header = MdSeHeader(content, level, underline_length=underline_length)
    assert str(header) == expected_output


def test_mdseheader_default_parameters() -> None:
    header = MdSeHeader("Default Header")
    assert str(header) == "Default Header\n===\n"
    assert header.level == 1
    assert header.indent == 0
    assert header.underline_length == 3
    assert header.newline_char == "\n"


def test_mdseheader_trailing_newlines_removed() -> None:
    with patch("mdfy.elements.seheader.logger") as mock_logger:
        header = MdSeHeader("Header\n\n")
        assert str(header) == "Header\n===\n"
        mock_logger.warning.assert_called_once_with(
            "Trailing newlines in setext header content are ignored."
        )


@pytest.mark.parametrize(
    "content, expected_error",
    [
        ("", "Setext header content must have at least non-whitespace character."),
        ("   ", "Setext header content must have at least non-whitespace character."),
        ("\n", "Setext header content must have at least non-whitespace character."),
        ("\t", "Setext header content must have at least non-whitespace character."),
    ],
    ids=["empty", "spaces", "newline", "tab"],
)
def test_mdseheader_invalid_content(content: str, expected_error: str) -> None:
    with pytest.raises(ValueError, match=expected_error):
        MdSeHeader(content)


@pytest.mark.parametrize(
    "level, expected_error",
    [
        (0, "Setext header level must be either 1 or 2."),
        (3, "Setext header level must be either 1 or 2."),
        (-1, "Setext header level must be either 1 or 2."),
        (10, "Setext header level must be either 1 or 2."),
    ],
    ids=["level0", "level3", "negative", "level10"],
)
def test_mdseheader_invalid_level(level: int, expected_error: str) -> None:
    with pytest.raises(ValueError, match=expected_error):
        MdSeHeader("Valid Content", level)


@pytest.mark.parametrize(
    "indent, expected_error",
    [
        (-1, "Indent must be in the range of 0 to 3."),
        (4, "Indent must be in the range of 0 to 3."),
        (10, "Indent must be in the range of 0 to 3."),
    ],
    ids=["negative", "indent4", "indent10"],
)
def test_mdseheader_invalid_indent(indent: int, expected_error: str) -> None:
    with pytest.raises(ValueError, match=expected_error):
        MdSeHeader("Valid Content", indent=indent)


@pytest.mark.parametrize(
    "underline_length, expected_error",
    [
        (0, "Setext header underline length must be at least 3."),
        (1, "Setext header underline length must be at least 3."),
        (2, "Setext header underline length must be at least 3."),
        (-1, "Setext header underline length must be at least 3."),
    ],
    ids=["length0", "length1", "length2", "negative"],
)
def test_mdseheader_invalid_underline_length(
    underline_length: int, expected_error: str
) -> None:
    with pytest.raises(ValueError, match=expected_error):
        MdSeHeader("Valid Content", underline_length=underline_length)


def test_mdseheader_complex_combination() -> None:
    header = MdSeHeader(
        "Complex\nMulti-line\nHeader", level=2, indent=2, underline_length=8
    )
    expected = "Complex\nMulti-line\nHeader\n  --------\n"
    assert str(header) == expected


def test_mdseheader_custom_newline_char() -> None:
    header = MdSeHeader("Header", newline_char="\r\n")
    assert str(header) == "Header\r\n===\n"

    header = MdSeHeader("Header", level=2, newline_char="\r")
    assert str(header) == "Header\r---\n"
