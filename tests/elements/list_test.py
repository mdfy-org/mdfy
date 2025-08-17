import pytest

from mdfy import MdList, MdText

TEST_CASES = [
    {
        "items": ["A", "B", "C"],
        "numbered": True,
        "expected_output": ("1. A\n" "1. B\n" "1. C"),
    },
    {
        "items": ["A", "B", "C"],
        "numbered": False,
        "expected_output": ("- A\n" "- B\n" "- C"),
    },
    {
        "items": ["A", ["B1", "B2"], "C"],
        "numbered": True,
        "expected_output": ("1. A\n" "    1. B1\n" "    1. B2\n" "1. C"),
    },
    {
        "items": ["A", ["B1", "B2", ["C1", "C2"], "B3"], "A"],
        "numbered": True,
        "indent": 2,
        "expected_output": (
            "1. A\n"
            "  1. B1\n"
            "  1. B2\n"
            "    1. C1\n"
            "    1. C2\n"
            "  1. B3\n"
            "1. A"
        ),
    },
    {
        "items": [
            MdText("That's a bold statement"),
            MdText("B"),
            MdText("Plain text"),
        ],
        "numbered": True,
        "expected_output": (
            "1. That's a bold statement\n" "1. B\n" "1. Plain text"
        ),
    },
]


@pytest.mark.parametrize("test_data", TEST_CASES)
def test_md_list(test_data: dict) -> None:
    items = test_data["items"]
    numbered = test_data["numbered"]
    indent = test_data.get("indent", 4)
    expected_output = test_data["expected_output"]

    md_list = MdList(items, numbered=numbered, indent=indent)
    assert str(md_list) == expected_output
