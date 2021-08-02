from pytest import mark
from app.roman_numerals import parse


# def test_roman_numeral_parser():
#     value = parse("IX")

#     assert value == 9

@mark.parametrize('s, expected', [("IX", 9), ("X", 10)])
def test_roman_numeral_parser(s, expected):
    result = parse(s)

    assert result == expected
