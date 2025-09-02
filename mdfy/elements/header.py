import warnings

from ._base import MdElement


class MdHeader(MdElement):
    """Represents a Markdown header.

    Attributes:
        content (str): The content of the header.
        level (int): The header level.
        indent (str): The indentation for the header.

    Examples:
        >>> from mdfy.elements import MdHeader
        >>>
        >>> header = MdHeader("This is a header")
        >>> print(header)
        # This is a header
        >>>
        >>> header = MdHeader("This is a header", level=2)
        >>> print(header)
        ## This is a header
    """

    def __init__(self, content: str, level: int = 1, indent: str = "") -> None:
        """Initializes an instance of the MdHeader class to represent a Markdown header.

        Args:
            content (str): The content of the header.
            level (int, optional): The header level. Should be in a range of 6 >= level >= 1. Defaults to 1.
            indent (str, optional): The indentation for the header. Defaults to "".
        """
        self.content = content
        if level < 1 or level > 6:
            warnings.warn(
                f"Header level {level} is out of range. Setting to 1."
            )

        self.level = level
        self.indent = indent

    def __str__(self) -> str:
        """Returns a string representation of the header in Markdown format.

        Returns:
            str: String representation of the header.
        """
        return self.indent + "#" * self.level + " " + self.content
