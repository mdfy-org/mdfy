from mdfy import MdText


def test_text_no_lark() -> None:
    text = MdText("[Hello:bold]")
    assert str(text) == "[Hello:bold]"
