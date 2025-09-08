import pytest

from mdfy import MdHorizontal


def test_md_horizontal_default() -> None:
    md_horizontal = MdHorizontal()
    assert str(md_horizontal) == "\n***\n", "Default content should be '***'"


def test_md_horizontal_custom_content() -> None:
    custom_content = "---"
    md_horizontal = MdHorizontal(content=custom_content)
    assert (
        str(md_horizontal) == f"\n{custom_content}\n"
    ), f"Content should be '{custom_content}'"


def test_md_horizontal_invalid_character() -> None:
    with pytest.warns(match="Horizontal content is not a valid character"):
        md_horizontal = MdHorizontal(content="+++")
        assert (
            str(md_horizontal) == "\n+++\n"
        ), "invalid character content should still be accepted"


def test_md_horizontal_short_content() -> None:
    with pytest.warns(match="Horizontal content not long enough"):
        md_horizontal = MdHorizontal(content="**")
        assert str(md_horizontal) == "\n**\n", "short content should still be accepted"


def test_md_horizontal_mixed_characters() -> None:
    with pytest.warns(match="Horizontal content should be made of a single character"):
        md_horizontal = MdHorizontal(content="*-*")
        assert (
            str(md_horizontal) == "\n*-*\n"
        ), "mixed character content should still be accepted"
