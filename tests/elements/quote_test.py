from mdfy import MdQuote, MdText


def test_mdquote_with_simple_string() -> None:
    quote = MdQuote("This is a simple quote.")
    assert str(quote) == "> This is a simple quote."


def test_mdquote_with_multi_line_string() -> None:
    content = """This is a multi-line
quote for testing."""
    quote = MdQuote(content)
    expected_output = """> This is a multi-line
> quote for testing."""
    assert str(quote) == expected_output


def test_mdquote_with_md_element() -> None:
    content = MdText("This is a quote using MdText.")
    quote = MdQuote(content)
    assert str(quote) == "> This is a quote using MdText."


def test_mdquote_with_empty_string() -> None:
    quote = MdQuote("")
    assert str(quote) == "> "
