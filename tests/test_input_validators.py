import pytest
from app.input_validators import validate_number, validate_args
from app.exceptions import InvalidInputError


def test_validate_number():
    assert validate_number("5") == 5.0


def test_validate_number_invalid():
    with pytest.raises(InvalidInputError):
        validate_number("abc")


def test_validate_args():
    a, b = validate_args(["3", "4"])
    assert a == 3
    assert b == 4


def test_validate_args_error():
    with pytest.raises(InvalidInputError):
        validate_args(["1"])