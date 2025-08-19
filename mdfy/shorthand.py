from typing import Optional, Union, Any
from .elements import (
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
from .elements._base import MdElement
from .elements.text_formatter import MdFormatter
from .mdfy import Mdfier


def code(code: str, inline: bool = False, syntax: str = "") -> MdCode:
    """Creates a code element."""
    return MdCode(code, inline=inline, syntax=syntax)


def header(content: str, level: int = 1) -> MdHeader:
    """Creates a header element."""
    return MdHeader(content, level=level)


def horizontal(content: str = "***") -> MdHorizontal:
    """Creates a horizontal rule element."""
    return MdHorizontal(content=content)


def image(src: str, alt: str = "") -> MdImage:
    """Creates an image element."""
    return MdImage(src, alt=alt)


def link(url: str, text: str = "", title: Optional[str] = None) -> MdLink:
    """Creates a link element."""
    return MdLink(url, text=text, title=title)


def list_item(
    items: list[Union[str, MdList]],
    depth: int = 0,
    indent: int = 4,
    numbered: bool = False,
) -> MdList:
    """Creates a list item element."""
    return MdList(items, depth=depth, indent=indent, numbered=numbered)


def quote(content: Union[str, MdElement]) -> MdQuote:
    """Creates a quote element."""
    return MdQuote(content)


def table(
    data: Union[dict[str, Any], list[dict[str, Any]]],
    header: Optional[list[str]] = None,
    row_labels: Optional[list[str]] = None,
    transpose: bool = False,
    precision: Union[None, int] = None,
) -> MdTable:
    """Creates a table element."""
    return MdTable(
        data,
        header=header,
        row_labels=row_labels,
        transpose=transpose,
        precision=precision,
    )


def text(
    content: str, formatter: Optional[MdFormatter] = None, no_style: bool = False
) -> MdText:
    """Creates a text element."""
    return MdText(content, formatter=formatter, no_style=no_style)


def toc(
    contents: Optional[list[Any]] = None, render_all: bool = False
) -> MdTableOfContents:
    """Creates a table of contents element."""
    return MdTableOfContents(contents, render_all=render_all)
