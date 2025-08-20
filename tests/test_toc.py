from pathlib import Path

import pytest

from mdfy import Mdfier, MdHeader, MdTableOfContents, MdText
from mdfy.types import MdWritableItem


def test_table_of_contents_basic(tmp_path: Path) -> None:
    """Test basic table of contents generation"""
    filepath = tmp_path / "test.md"
    mdfier = Mdfier.from_filepath(filepath)

    # Write content with table of contents
    content: list[MdWritableItem] = [
        MdHeader("First Section", 1),
        MdHeader("Subsection A", 2),
        MdHeader("Subsection B", 2),
        MdText("Some text"),
        MdHeader("Second Section", 1),
        MdHeader("Another Subsection", 2),
    ]

    mdfier.write([MdTableOfContents(contents=content), *content])

    # Read the generated content
    file_content = filepath.read_text()

    # Expected table of contents
    expected_toc = "\n".join(
        [
            "- [First Section](#first-section)",
            "  - [Subsection A](#subsection-a)",
            "  - [Subsection B](#subsection-b)",
            "- [Second Section](#second-section)",
            "  - [Another Subsection](#another-subsection)",
            "",
        ]
    )

    assert expected_toc in file_content


def test_table_of_contents_with_mdfier_contents(tmp_path: Path) -> None:
    """Test table of contents using Mdfier's content list"""
    filepath = tmp_path / "test.md"
    mdfier = Mdfier.from_filepath(filepath)

    # Write content with table of contents
    content: list[MdWritableItem] = [
        MdTableOfContents(),  # No contents provided, will use Mdfier's content
        MdHeader("Section 1", 1),
        MdHeader("Section 2", 1),
    ]
    mdfier.write(content)

    # Read the generated content
    result = filepath.read_text()

    # Expected table of contents
    expected_toc = "\n".join(
        [
            "- [Section 1](#section-1)",
            "- [Section 2](#section-2)",
            "",
        ]
    )

    assert expected_toc in result


def test_table_of_contents_in_the_middle_of_contents(tmp_path: Path) -> None:
    """Test table of contents using Mdfier's content list"""
    filepath = tmp_path / "test.md"
    mdfier = Mdfier.from_filepath(filepath)

    # Write content with table of contents
    content: list[MdWritableItem] = [
        MdHeader("Section 1", 1),
        MdHeader("Table of Contents", 2),
        MdTableOfContents(),
        MdHeader("Section 2", 1),
        MdHeader("Section 2.1", 2),
        MdHeader("Section 2.2", 2),
        MdHeader("Section 3", 1),
    ]
    mdfier.write(content)

    # Read the generated content
    result = filepath.read_text()

    # Expected table of contents
    expected_toc = "\n".join(
        [
            "## Table of Contents",
            "",
            "- [Section 2](#section-2)",
            "  - [Section 2.1](#section-2.1)",
            "  - [Section 2.2](#section-2.2)",
            "- [Section 3](#section-3)",
            "",
        ]
    )

    print(expected_toc)
    print(result)
    assert expected_toc in result


def test_table_of_contents_empty() -> None:
    """Test table of contents with empty content list"""
    toc = MdTableOfContents(contents=[])
    with pytest.raises(ValueError, match="No contents provided.*"):
        toc.render()


def test_table_of_contents_standalone() -> None:
    """Test table of contents generation without Mdfier"""
    contents: list[MdWritableItem] = [
        MdHeader("First Section", 1),
        MdHeader("Subsection A", 2),
        MdHeader("Subsection B", 2),
        MdHeader("Second Section", 1),
        MdHeader("Another Subsection", 2),
    ]

    toc = MdTableOfContents(contents=contents)
    result = toc.render()

    expected = "\n".join(
        [
            "- [First Section](#first-section)",
            "  - [Subsection A](#subsection-a)",
            "  - [Subsection B](#subsection-b)",
            "- [Second Section](#second-section)",
            "  - [Another Subsection](#another-subsection)",
            "",
        ]
    )

    assert result == expected


def test_table_of_contents_no_contents() -> None:
    """Test table of contents with no contents raises error"""
    toc = MdTableOfContents()
    try:
        toc.render()
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == (
            "No contents provided. "
            "Either contents argument or _contents attribute must be provided."
        )
