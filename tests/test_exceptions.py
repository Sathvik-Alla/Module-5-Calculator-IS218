from app.exceptions import CalculatorError, InvalidInputError, DivisionByZeroError


def test_exception_inheritance():
    assert issubclass(InvalidInputError, CalculatorError)
    assert issubclass(DivisionByZeroError, CalculatorError)