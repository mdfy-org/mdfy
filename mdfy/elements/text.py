from typing import Optional

from mdfy.elements._base import MdElement
from mdfy.elements.text_formatter import MdFormatter

try:
    from mdfy.elements.formatter.lark_formatter import MdTextFormatter

    _formatter_available = True
except ImportError:
    _formatter_available = False


class MdText(MdElement):
    """MdElementt class to handle the text and styling of text.

    Attributes:
        content (str): The content string containing potential style markers.
        formatter (MdFormatter): The formatter to apply styling to the content.

    Examples:
        >>> # If you have installed mdfy[styled-text]
        >>> from mdfy import MdText
        >>> try:
        >>>   import lark
        >>> except ModuleNotFoundError:
        >>>   print("Please install mdfy[styled-text] to use MdText with styles.")
        >>>   exit(0)
        >>>
        >>> text = MdText("This is [bold:bold] text.")
        >>> print(text)
        This is **bold** text.
        >>> MdText("[This is underline text:underline].").to_str()
        <u>This is underline text</u>.
        >>> MdText("[This is [nested:bold] style text:underline].").to_str()
        <u>This is **nested** style text</u>.
        >>> MdText("You can use aliases e.g. [st:st]  [bd:bo].").to_str()
        You can use aliases e.g. ***st***  **bd**.

    Note:
        Available style patterns:
            - strong: bold text (e.g. `***strong***`)
            - bold: bold text (e.g. `**bold**`)
            - italic: italic text (e.g. `*italic*`)
            - not: strike-through text (e.g. `~~strike-through~~`)
            - underline: underlined text (e.g. `<u>underlined</u>`)
            - code: inline code (e.g. `code`)

        Also, the following aliases are available for the style patterns:
            - strong: st
            - bold: bo, bd
            - italic: it
            - not: no, nt
            - underline: un, ul
            - code: cd, quote
    """

    def __init__(
        self,
        content: str,
        formatter: Optional[MdFormatter] = None,
        no_style: bool = False,
    ) -> None:
        """Initializes an instance of the MdText class to handle the text and styling of text.

        Args:
            content (str): The content string containing potential style markers.
            formatter (MdFormatter, optional): The formatter to apply styling to the content.
                                                     Defaults to None.
            no_style (bool, optional): If True, no style will be applied to the content.
                                       Defaults to False.
        """

        self.content = content
        self.formatter = formatter
        self.no_style = no_style

        if self.formatter is None and _formatter_available and not no_style:
            self.formatter = MdTextFormatter()

    def __str__(self) -> str:
        """Returns the styled content as per the specified style markers.

        Returns:
            str: Formatted markdown string with the appropriate styles applied.
        """
        result = self.content
        if self.formatter and not self.no_style:
            result = self.formatter.format(result)

        return result

    def __add__(self, other: "MdText") -> "MdText":
        """Adds two MdText objects together.

        Args:
            other (MdText): The other MdText object to be added.

        Returns:
            MdText: A new MdText object containing the concatenated content of the two objects.
        """
        return MdText(str(self) + str(other))
