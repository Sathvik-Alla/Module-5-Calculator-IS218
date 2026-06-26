class CalculatorError(Exception):
    """Base exception for calculator"""


class InvalidOperationError(CalculatorError):
    pass


class InvalidInputError(CalculatorError):
    pass


class DivisionByZeroError(CalculatorError):
    pass