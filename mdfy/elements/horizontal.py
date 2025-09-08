import warnings

from ._base import MdElement


_ACCEPTABLE_SYMBOLS = {"*", "-", "_"}


class MdHorizontal(MdElement):
    """Represents a Markdown horizontal rule.

    Attributes:
        content (str): The content for representing the horizontal rule.

    Examples:
        >>> from mdfy.elements import MdHorizontal
        >>>
        >>> horizontal = MdHorizontal()
        >>> print(horizontal)
        ***
        >>>
        >>> horizontal = MdHorizontal("---")
        >>> print(horizontal)
        ---
    """

    def __init__(self, content: str = "***", indent: str = "") -> None:
        """Initializes an instance of the MdHorizontal class to represent a Markdown horizontal rule.

        Args:
            content (str, optional): The content of the horizontal rule. Defaults to "***".
        """
        content_chars = set(list(content))
        if len(content_chars) > 1:
            warnings.warn(f"Horizontal content should be made of a single character")
        if not set(list(content)) <= _ACCEPTABLE_SYMBOLS:
            warnings.warn(f"Horizontal content is not a valid character")
        if len(content) < 3:
            warnings.warn(f"Horizontal content not long enough")
        self.content = content
        self.indent = indent

    def __str__(self) -> str:
        return f"\n{self.indent}{self.content}\n"
