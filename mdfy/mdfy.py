from io import TextIOBase
from pathlib import Path
from types import TracebackType
from typing import Optional, Type, Union, Iterable
import logging

from .elements import MdTableOfContents
from .utils import flattern
from .types import MdContents

logger = logging.getLogger(__name__)


class Mdfier:
    """Writes Markdown content to a file.

    Attributes:
        filepath (Path): The path to the file.

    Examples:
        >>> from mdfy import Mdfier, MdHeader, MdQuote, MdText
        >>> # Writing Markdown content to a file
        >>> mdfier = Mdfier("/tmp/quote.md")
        >>> mdfier.write([
        ...     MdHeader("Hello, world!", 1),
        ...     MdQuote("This is a quote.")
        ... ])
        >>>
        >>> with open("/tmp/quote.md") as file:
        ...     print(file.read())
        ...
        # Hello, world!
        > This is a quote.

        from mdfy import MdHeader, MdQuote, MdText
        >>> mdfier = Mdfier("/tmp/nest.md")
        >>> # Nested content will be flattened
        >>> mdfier.write([
        ...     MdHeader("Hello, world!", 1),
        ...     [
        ...         MdText(f"{i} * {i} = {i * i}")
        ...         for i in range(1, 3)
        ...     ]
        ... ])
        >>> with open("/tmp/nest.md") as file:
        ...     print(file.read())
        ...
        # Hello, world!
        1 * 1 = 1
        2 * 2 = 4
    """

    def __init__(
        self,
        filepath: Optional[Path] = None,
        file_object: Optional[TextIOBase] = None,
        encoding: str = "utf-8",
    ) -> None:
        """Initializes an instance of the Mdfier class to write Markdown content to a file.

        Args:
            filepath (Path | None): The path to the file. If None, the file_object must be provided.
            file_object (TextIOBase | None): The file object to write to. If None, the filepath must be provided.
            encoding (str): The encoding of the file. Defaults to "utf-8".
        """

        self._filepath = filepath
        self._file_object: Optional[TextIOBase] = file_object
        self._encoding = encoding

    @classmethod
    def from_filepath(
        cls,
        filepath: Union[str, Path],
        encoding: str = "utf-8",
        create_dir_if_not_exist: bool = True,
    ) -> "Mdfier":
        """Creates an instance of the Mdfier class to write Markdown content to a file.

        Args:
            filepath (Union[str, Path]): The path to the file.
            encoding (str): The encoding of the file.

        Returns:
            Mdfier: An instance of the Mdfier class.
        """

        filepath = Path(filepath)
        if create_dir_if_not_exist:
            filepath.parent.mkdir(
                parents=create_dir_if_not_exist, exist_ok=create_dir_if_not_exist
            )

        return cls(filepath=filepath, encoding=encoding)

    @classmethod
    def from_file(cls, file_object: TextIOBase) -> "Mdfier":
        """Creates an instance of the Mdfier class to write Markdown content to a  object.

        Args:
            file_object (TextIOBase): The file object to write to.

        Returns:
            Mdfier: An instance of the Mdfier class.
        """

        return cls(file_object=file_object)

    def __enter__(self) -> "Mdfier":
        """Returns the Mdfier instance.

        Returns:
            Mdfier: The Mdfier instance.
        """

        if self._filepath is not None:
            self._file_object = self._filepath.open("w", encoding=self._encoding)

        if self._file_object is None:
            raise ValueError(
                "No target file is specified. Please use `from_filepath` or `from_file` to create an instance."
            )

        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Writes the Markdown content to the file.

        Args:
            exc_type (type): The type of the exception.
            exc_value (Exception): The exception that was raised.
            traceback (Traceback): The traceback of the exception.
        """
        if self._file_object is None:
            return
        self._file_object.close()

    @classmethod
    def stringify(cls, contents: MdContents, separator: str = "\n") -> str:
        """Converts the given Markdown content to a string.

        Args:
            content (Union[str, MdElement]): The Markdown content to convert to a string.
        """

        flattened_contents = flattern(contents)

        markdown_parts = []
        for i, element in enumerate(flattened_contents):
            if isinstance(element, MdTableOfContents):
                markdown_parts.append(element.render(flattened_contents, i))
            else:
                markdown_parts.append(str(element))

        return separator.join(markdown_parts)

    def write(self, contents: MdContents) -> None:
        """Writes the given Markdown content to the file.

        Args:
            content (Union[str, MdElement]): The Markdown content to write to the file.
        """

        if not isinstance(contents, Iterable):
            contents = [contents]

        markdown = self.stringify(contents)
        if self._file_object is not None:
            self._file_object.write(markdown + "\n")
        elif self._filepath is not None:
            self._filepath.write_text(markdown + "\n", encoding=self._encoding)
        else:
            raise ValueError(
                "No target file is specified. Please use `from_filepath` or `from_file` to create an instance."
            )
