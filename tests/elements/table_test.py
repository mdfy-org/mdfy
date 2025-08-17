import pytest

from mdfy import MdTable


# Test initialization with dictionary
def test_initialization_with_dict() -> None:
    data = {"name": "John", "age": 30}
    table = MdTable(data)
    assert isinstance(table, MdTable)
    md_output = str(table)
    # expected_output = "| name | age |\n" "| --- | --- |\n" "| John | 30 |"
    expected_output = "| name | age |\n" "| --- | --- |\n" "| John | 30 |"
    assert md_output == expected_output


# Test initialization with list of dictionaries
def test_initialization_with_list() -> None:
    data = [{"name": "John", "age": 30}, {"name": "Doe", "age": 25}]
    table = MdTable(data)
    assert isinstance(table, MdTable)
    md_output = str(table)
    expected_output = (
        "| name | age |\n" "| --- | --- |\n" "| John | 30 |\n" "| Doe | 25 |"
    )
    assert md_output == expected_output


# Test the creation of a regular markdown table from dictionary data
def test__to_md_table() -> None:
    data = [{"name": "John", "age": 30}]
    table = MdTable(data)
    md_output = str(table)
    # fmt: off
    expected_output = (
        "| name | age |\n"
        "| --- | --- |\n"
        "| John | 30 |"
    )
    # fmt: on
    assert md_output == expected_output


# Test the creation of a transposed markdown table from dictionary data
def test_transposed_table() -> None:
    data = [{"name": "John", "age": 30}]
    table = MdTable(data, transpose=True)
    md_output = str(table)
    # fmt: off
    expected_output = (
        "| | |\n"
        "| --- | --- |\n"
        "| name | John |\n"
        "| age | 30 |"
    )
    # fmt: on
    assert md_output == expected_output


# Test custom headers
def test_custom_headers() -> None:
    data = [{"name": "John", "age": 30}]
    table = MdTable(data, header=["Full Name", "Years"])
    md_output = str(table)
    # fmt: off
    expected_output = (
        "| Full Name | Years |\n"
        "| --- | --- |\n"
        "| John | 30 |"
    )
    # fmt: on
    assert md_output == expected_output


# Test row labels
def test_row_labels() -> None:
    data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    table = MdTable(data, row_labels=["Person 1", "Person 2"])
    md_output = str(table)
    # fmt: off
    expected_output = (
        "| | name | age |\n"
        "| --- | --- | --- |\n"
        "| Person 1 | John | 30 |\n"
        "| Person 2 | Jane | 25 |"
    )
    # fmt: on
    assert md_output == expected_output


# Test the floating point number precision
def test_precision() -> None:
    data = [{"value": 3.14159265359}]
    table = MdTable(data, precision=2)
    md_output = str(table)
    # fmt: off
    expected_output = (
        "| value |\n"
        "| --- |\n"
        "| 3.14 |"
    )
    # fmt: on
    assert md_output == expected_output


# Test nested dictionary flattening
def test_flatten_dict() -> None:
    data = {"user": {"name": "John", "details": {"age": 30, "location": "Tokyo"}}}
    table = MdTable(data)
    md_output = str(table)
    expected_output = (
        "| user.name | user.details.age | user.details.location |\n"
        "| --- | --- | --- |\n"
        "| John | 30 | Tokyo |"
    )
    assert md_output == expected_output


# Test MdText integration
def test_mdtext_integration() -> None:
    from mdfy import MdText

    data = {"text": MdText("bold")}
    table = MdTable(data)
    md_output = str(table)
    # fmt: off
    expected_output = (
        "| text |\n"
        "| --- |\n"
        "| bold |"
    )
    # fmt: on
    assert md_output == expected_output


# Test the exception for invalid input
def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        MdTable("invalid input")  # type: ignore
