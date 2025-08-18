import tempfile
from pathlib import Path

from mdfy import Mdfier, MdHeader, MdText, MdLink, MdElement


def test_mdfy_init_from_filepath() -> None:
    tmp_output_path = Path(tempfile.gettempdir(), "output.md")
    mdfier = Mdfier(tmp_output_path)
    assert mdfier._filepath == tmp_output_path
    assert mdfier._file_object is None
    assert mdfier._encoding == "utf-8"


def test_mdfy_init_from_file_object() -> None:
    tmp_output_path = Path(tempfile.gettempdir(), "output.md")
    with tmp_output_path.open("w", encoding="utf-8") as file_object:
        mdfier = Mdfier.from_file(file_object)
        assert mdfier._filepath is None
        assert mdfier._textio == file_object
        assert mdfier._encoding == "utf-8"


def test_mdfy_write() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [
            MdHeader("Hello, MDFY!"),
            MdText("Life is like a bicycle."),
        ]
        tmp_output_path = Path(tmp_dir, "output.md")
        Mdfier.from_filepath(tmp_output_path).write(contents)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# Hello, MDFY!\n"
            assert lines[1] == "Life is like a bicycle.\n"


def test_mdfy_write_using_file_object() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [
            MdHeader("Hello, MDFY!"),
            MdText("Life is like a bicycle."),
        ]
        tmp_output_path = Path(tmp_dir, "output.md")
        with tmp_output_path.open("w", encoding="utf-8") as file_object:
            mdfier = Mdfier.from_file(file_object=file_object)
            mdfier.write(contents)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# Hello, MDFY!\n"
            assert lines[1] == "Life is like a bicycle.\n"


def test_mdfy_write_with_statement() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [
            MdHeader("Hello, MDFY!"),
            MdText("Life is like a bicycle."),
        ]
        tmp_output_path = Path(tmp_dir, "output.md")
        mdfier = Mdfier.from_filepath(tmp_output_path)
        with mdfier as mdfier:
            for content in contents:
                mdfier.write(content)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# Hello, MDFY!\n"
            assert lines[1] == "Life is like a bicycle.\n"
            assert mdfier._file_object and mdfier._file_object.closed


def test_mdfy_write_in_utf8() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [MdHeader("こんにちは")]
        tmp_output_path = Path(tmp_dir, "output.md")
        mdier = Mdfier.from_filepath(tmp_output_path)
        with mdier as mdfier:
            for content in contents:
                mdfier.write(content)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# こんにちは\n"
            assert mdfier._file_object and mdfier._file_object.closed


def test_mdfy_nested_contents() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents: list[MdElement | list[MdElement | str]] = [
            MdHeader("Hello, MDFY!"),
            [
                MdText("This is a nested content."),
                MdText("This is another nested content."),
                (MdLink("url", "Click me!")),
                "This is a simple text.",
            ],
        ]
        tmp_output_path = Path(tmp_dir, "output.md")
        Mdfier.from_filepath(tmp_output_path).write(contents)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# Hello, MDFY!\n"
            assert lines[1] == "This is a nested content.\n"
            assert lines[2] == "This is another nested content.\n"
            assert lines[3] == "[Click me!](url)\n"
            assert lines[4] == "This is a simple text.\n"
