import logging

from ._base import MdElement

logger = logging.getLogger(__name__)


class MdIndentCode(MdElement):
    """Represents Markdown indented code block.

    Indented code blocks follow GitHub Flavored Markdown format:
    - Add 4+ spaces indentation
    - Preserve literal content (no Markdown parsing)
    - Preserve trailing line endings
    - Support separation by blank lines
    - Require blank line before when following paragraph

    Attributes:
        code (str): The code string.

    Examples:
        >>> code = MdIndentCode("print('Hello World!')")
        >>> print(code)
            print('Hello World!')
        >>> code = MdIndentCode("line1\\nline2")
        >>> print(code)
            line1
            line2
    """

    def __init__(self, code: str, indent: int = 4, newline: str = "\n") -> None:
        """Initializes an instance of the MdIndentCode class.

        Args:
            code (str): The code string.
            indent (int, optional): The number of spaces to indent the code block. Defaults to 4.
            newline (str, optional): The newline character to use. Defaults to "\n".
        """

        if code is None:
            raise ValueError("Code content cannot be None.")

        self.code = code

        if indent < 4:
            logger.warning(
                "Indentation for indented code blocks should be at least 4 spaces. "
                "Setting indent to 4 spaces."
            )
            indent = 4
        self.indent = indent

        self.newline = newline

    def __str__(self) -> str:
        """Returns a string representation of the indented code in Markdown format.

        Returns:
            str: String representation of the indented code with 4-space indentation.

        The method:
        - Adds 4 spaces indentation to each line
        - Preserves literal content (no Markdown parsing)
        - Preserves trailing line endings
        - Supports separation by blank lines
        """

        lines = self.code.split("\n")
        indented_lines = []

        for line in lines:
            indented_lines.append((" " * self.indent) + line)

        return self.newline.join(indented_lines) + self.newline
