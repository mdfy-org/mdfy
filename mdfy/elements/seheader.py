import logging
from textwrap import dedent

from ._base import MdElement

logger = logging.getLogger(__name__)


class MdSeHeader(MdElement):
    """Represents a Markdown setext header.

    Attributes:
        content (str): The content of the header. multi-line content is supported.
        level (int): The header level. Only 1 or 2 are supported.

    Examples:
        >>> from mdfy.elements import MdSeHeader
        >>>
        >>> header = MdSeHeader("This is a header")
        >>> print(header)
        This is a header
        ===
        >>>
        >>> header = MdSeHeader("This is a header", level=2)
        >>> print(header)
        This is a header
        ---
    """

    def __init__(
        self,
        content: str,
        level: int = 1,
        indent: int = 0,
        underline_length: int = 3,
        newline_char: str = "\n",
    ) -> None:
        """Initializes an instance of the MdSeHeader class to represent a Markdown header.

        Args:
            content (str): The content of the header. multi-line content is supported.
            level (int, optional): The header level. Defaults to 1.
            indent (int, optional): The number of spaces to indent the header underline. Defaults to 0. Should be in a range of 0 <= indent <= 3.
            underline_length (int, optional): The minimum length of the underline. Defaults to 3.
            newline_char (str, optional): The newline character to use. Defaults to "\n".
        """
        if len(content.strip()) < 1:
            raise ValueError(
                "Setext header content must have at least non-whitespace character."
            )
        if content.endswith("\n"):
            content = content.rstrip("\n")
            logger.warning("Trailing newlines in setext header content are ignored.")
        self.content = content

        if not 0 <= indent <= 3:
            raise ValueError("Indent must be in the range of 0 to 3.")
        self.indent = indent

        if level not in (1, 2):
            raise ValueError("Setext header level must be either 1 or 2.")
        self.level = level

        if underline_length < 3:
            raise ValueError("Setext header underline length must be at least 3.")
        self.underline_length = underline_length

        self.newline_char = newline_char

    def __str__(self) -> str:
        """Returns a string representation of the header in Markdown format.

        Returns:
            str: String representation of the header.
        """
        underline_char = "=" if self.level == 1 else "-"
        underline = underline_char * self.underline_length
        return f"{self.content}{self.newline_char}{' ' * self.indent}{underline}\n"
