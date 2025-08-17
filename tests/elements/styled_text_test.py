import pytest

from mdfy import MdText

lark = pytest.importorskip("lark")


@pytest.mark.styled_text
def test_text_concatenation() -> None:
    text1 = MdText("[Hello:bold]")
    text2 = MdText("[World:italic]")
    combined = text1 + text2
    assert str(combined) == "**Hello***World*"


@pytest.mark.styled_text
def test_nested_style() -> None:
    text = MdText("[italic in bold is = [strong:italic]:bold]")
    assert str(text) == "**italic in bold is = *strong***"


@pytest.mark.styled_text
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Plain text", "Plain text"),
        ("[Hello:italic] and World", "*Hello* and World"),
        ("[Hello:not] and World", "~~Hello~~ and World"),
        ("[Hello:bold] and [World:bold]", "**Hello** and **World**"),
        ("[Hello:bold] and [World:italic]", "**Hello** and *World*"),
        ("[Hello:strong] and [World:strong]", "***Hello*** and ***World***"),
        ("this is [quoted:quote] text", "this is `quoted` text"),
        ("[Hello:underline] and [World:underline]", "<u>Hello</u> and <u>World</u>"),
        (
            "This is [underline:underline] text in middle",
            "This is <u>underline</u> text in middle",
        ),
        (
            "This text has : in [not styled:bold] part",
            "This text has : in **not styled** part",
        ),
        (
            "[ユニコード文字列:underline]に対応してるか",
            "<u>ユニコード文字列</u>に対応してるか",
        ),
        (
            "[[Boldalic!!!:italic]:bold]",
            "***Boldalic!!!***",
        ),
        (
            "[italic in bold is = [strong:italic]:bold]",
            "**italic in bold is = *strong***",
        ),
        (
            "[This is [italic:italic] and [bold:bold] in underline:underline]",
            "<u>This is *italic* and **bold** in underline</u>",
        ),
    ],
)
def test_various_texts(input_text: str, expected_output: str) -> None:
    text = MdText(input_text)
    assert str(text) == expected_output


@pytest.mark.styled_text
def test_no_style() -> None:
    text = MdText("No style text.", no_style=True)
    assert str(text) == "No style text."
    text = MdText("[No style text:italic]", no_style=True)
    assert str(text) == "[No style text:italic]"


@pytest.mark.styled_text
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Plain text", "Plain text"),
        ("[Hello] and World", "[Hello] and World"),
        ("[[Hello:bold]] and World", "[**Hello**] and World"),
        ("[[Hello]] and World", "[[Hello]] and World"),
    ],
)
def test_text_with_bracket_but_no_style(input_text: str, expected_output: str) -> None:
    text = MdText(input_text)
    assert str(text) == expected_output


@pytest.mark.styled_text
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("[Hello:bold", "[Hello:bold"),
        ("Hello]", "Hello]"),
        ("[Hello:bold]]", "[Hello:bold]]"),
    ],
)
def test_fallback_when_parse_error(input_text: str, expected_output: str) -> None:
    text = MdText(input_text)
    assert str(text) == expected_output
