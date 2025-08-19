from io import StringIO

from mdfy.shorthand import (
    code,
    header,
    horizontal,
    image,
    link,
    list_item,
    quote,
    table,
    text,
    toc,
)
from mdfy import (
    MdCode,
    MdHeader,
    MdHorizontal,
    MdImage,
    MdLink,
    MdList,
    MdQuote,
    MdTable,
    MdTableOfContents,
    MdText,
)
from mdfy.mdfy import Mdfier


def test_code():
    """Test code() shorthand function equals MdCode."""
    shorthand = code("print('hello')", inline=True, syntax="python")
    direct = MdCode("print('hello')", inline=True, syntax="python")

    assert str(shorthand) == str(direct)
    assert shorthand.code == direct.code
    assert shorthand.inline == direct.inline
    assert shorthand.syntax == direct.syntax


def test_header():
    """Test header() shorthand function equals MdHeader."""
    shorthand = header("Test Header", level=2)
    direct = MdHeader("Test Header", level=2)

    assert str(shorthand) == str(direct)
    assert shorthand.content == direct.content
    assert shorthand.level == direct.level


def test_horizontal():
    """Test horizontal() shorthand function equals MdHorizontal."""
    shorthand = horizontal("---")
    direct = MdHorizontal("---")

    assert str(shorthand) == str(direct)
    assert shorthand.content == direct.content


def test_image():
    """Test image() shorthand function equals MdImage."""
    shorthand = image("test.png", alt="Test Image")
    direct = MdImage("test.png", alt="Test Image")

    assert str(shorthand) == str(direct)
    assert shorthand.src == direct.src
    assert shorthand.alt == direct.alt


def test_link():
    """Test link() shorthand function equals MdLink."""
    shorthand = link("http://test.com", text="Test", title="Test Site")
    direct = MdLink("http://test.com", text="Test", title="Test Site")

    assert str(shorthand) == str(direct)
    assert shorthand.url == direct.url
    assert shorthand.text == direct.text
    assert shorthand.title == direct.title


def test_list_item():
    """Test list_item() shorthand function equals MdList."""
    shorthand = list_item(["item1", "item2"], depth=1, indent=2, numbered=True)
    direct = MdList(["item1", "item2"], depth=1, indent=2, numbered=True)

    assert str(shorthand) == str(direct)
    assert shorthand.items == direct.items
    assert shorthand.depth == direct.depth
    assert shorthand.indent == direct.indent
    assert shorthand.numbered == direct.numbered


def test_quote():
    """Test quote() shorthand function equals MdQuote."""
    shorthand = quote("This is a quote")
    direct = MdQuote("This is a quote")

    assert str(shorthand) == str(direct)
    assert shorthand.content == direct.content


def test_table():
    """Test table() shorthand function equals MdTable."""
    data = {"Name": "John", "Age": 30}
    shorthand = table(data, header=["Full Name", "Years"], transpose=True, precision=2)
    direct = MdTable(data, header=["Full Name", "Years"], transpose=True, precision=2)

    assert str(shorthand) == str(direct)
    assert shorthand.header == direct.header
    assert shorthand.transpose == direct.transpose
    assert shorthand.precision == direct.precision


def test_text():
    """Test text() shorthand function equals MdText."""
    shorthand = text("Hello world", no_style=True)
    direct = MdText("Hello world", no_style=True)

    assert str(shorthand) == str(direct)
    assert shorthand.content == direct.content
    assert shorthand.no_style == direct.no_style


def test_toc():
    """Test toc() shorthand function equals MdTableOfContents."""
    contents = [header("Section 1"), header("Section 2")]
    shorthand = toc(contents=contents, render_all=True)
    direct = MdTableOfContents(contents=contents, render_all=True)

    # Both should have the same internal state
    assert shorthand._contents == direct._contents
    assert shorthand._render_all == direct._render_all
