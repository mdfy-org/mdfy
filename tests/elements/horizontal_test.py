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
    with pytest.warns(UserWarning, match="Horizontal content is not a valid character"):
        md_horizontal = MdHorizontal(content="+++")
        assert (
            str(md_horizontal) == "\+++\n"
        ), "invalid character content should still be accepted"


def test_md_horizontal_short_content() -> None:
    with pytest.warns(UserWarning, match="Horizontal content not long enough"):
        md_horizontal = MdHorizontal(content="**")
        assert (
            str(md_horizontal) == "\n**\n"
        ), "short content should still be accepted"


def test_md_horizontal_long_indent() -> None:
    with pytest.warns(UserWarning, match="Horizontal indent too long"):
        md_horizontal = MdHorizontal(indent="    ")
        assert (
            str(md_horizontal) == "\n   ***\n"
        ), "indent should be truncated to 3 spaces"
