from mdfy.elements.indent_code import MdIndentCode


def test_indent_code_single_line() -> None:
    code = MdIndentCode("print('Hello, World!')")
    expected = "    print('Hello, World!')\n"
    assert str(code) == expected


def test_indent_code_multiple_lines() -> None:
    code_content = "print('Hello, World!')\nprint('MDFY!')"
    code = MdIndentCode(code_content)
    expected = "    print('Hello, World!')\n    print('MDFY!')\n"
    assert str(code) == expected


def test_indent_code_with_empty_lines() -> None:
    code_content = "line1\n\nline3"
    code = MdIndentCode(code_content)
    expected = "    line1\n    \n    line3\n"
    assert str(code) == expected


def test_indent_code_empty_string() -> None:
    code = MdIndentCode("")
    expected = "    \n"
    assert str(code) == expected


def test_indent_code_preserves_trailing_whitespace() -> None:
    code_content = "code with spaces   \nmore code  "
    code = MdIndentCode(code_content)
    expected = "    code with spaces   \n    more code  \n"
    assert str(code) == expected


def test_indent_code_preserves_literal_content() -> None:
    # Test that markdown characters are preserved literally
    code_content = (
        "# This is not a header\n**This is not bold**\n`This is not inline code`"
    )
    code = MdIndentCode(code_content)
    expected = "    # This is not a header\n    **This is not bold**\n    `This is not inline code`\n"
    assert str(code) == expected


def test_indent_code_with_tabs() -> None:
    code_content = "def function():\n\treturn 'hello'"
    code = MdIndentCode(code_content)
    expected = "    def function():\n    \treturn 'hello'\n"
    assert str(code) == expected
