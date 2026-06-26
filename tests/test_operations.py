import pytest
from app.operations import OperationFactory
from app.exceptions import DivisionByZeroError


def test_add():
    op = OperationFactory.get_operation("add")
    assert op.execute(2, 3) == 5


def test_subtract():
    op = OperationFactory.get_operation("subtract")
    assert op.execute(5, 3) == 2


def test_multiply():
    op = OperationFactory.get_operation("multiply")
    assert op.execute(3, 4) == 12


def test_divide():
    op = OperationFactory.get_operation("divide")
    assert op.execute(10, 2) == 5


def test_divide_by_zero():
    op = OperationFactory.get_operation("divide")
    with pytest.raises(DivisionByZeroError):
        op.execute(10, 0)


def test_power():
    op = OperationFactory.get_operation("power")
    assert op.execute(2, 3) == 8


def test_root():
    op = OperationFactory.get_operation("root")
    assert round(op.execute(9, 2), 5) == 3


def test_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.get_operation("invalid")