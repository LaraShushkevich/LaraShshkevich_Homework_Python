import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    (" Snow", "Snow"),
    (" Hello World", "Hello World"),
    ("Book", "Book")
    ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, simbol, expected", [
    ("Snow", "S", True),
    ("Book", "W", False),
    ("Hello,World", " ", False)
    ])
def test_contains_positive(input_str, simbol, expected):
    assert string_utils.contains(input_str, simbol) == expected

@pytest.mark.parametrize("input_str, simbol, expected", [
    ("Snow", "S", "now"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello,World", ",", "HelloWorld")
])
def test_delete_symbol_positive(input_str, simbol, expected):
    assert string_utils.delete_symbol(input_str, simbol) == expected



@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, simbol, expected", [
    (" ", "", True),
    ("", "", True),
    ("", " ", False)
    ])
def test_contains_negative(input_str, simbol, expected):
    assert string_utils.contains(input_str, simbol) == expected

@pytest.mark.parametrize("input_str, simbol, expected", [
    ("Hello", "", "Hello"),
    ("", "", ""),
    ])
def test_delete_symbol_negative(input_str, simbol, expected):
    assert string_utils.delete_symbol(input_str, simbol) == expected

