import tempfile
from pathlib import Path

from mdfy import Mdfier, MdHeader, MdText, MdLink, MdElement


def test_mdfy_write() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [
            MdHeader("Hello, MDFY!"),
            MdText("Life is like a bicycle."),
        ]
        tmp_output_path = Path(tmp_dir, "output.md")
        Mdfier(tmp_output_path).write(contents)

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
        mdfier = Mdfier(tmp_output_path)
        with mdfier as mdfier:
            for content in contents:
                mdfier.write(content)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# Hello, MDFY!\n"
            assert lines[1] == "Life is like a bicycle.\n"
            assert mdfier.file_object and mdfier.file_object.closed


def test_mdfy_write_in_utf8() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [MdHeader("こんにちは")]
        tmp_output_path = Path(tmp_dir, "output.md")
        mdier = Mdfier(tmp_output_path)
        with mdier as mdfier:
            for content in contents:
                mdfier.write(content)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# こんにちは\n"
            assert mdfier.file_object and mdfier.file_object.closed


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
        Mdfier(tmp_output_path).write(contents)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# Hello, MDFY!\n"
            assert lines[1] == "This is a nested content.\n"
            assert lines[2] == "This is another nested content.\n"
            assert lines[3] == "[Click me!](url)\n"
            assert lines[4] == "This is a simple text.\n"
