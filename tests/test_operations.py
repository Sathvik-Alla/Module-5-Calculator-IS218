import pytest
from app.operations import OperationFactory
from app.operations import Operation
from app.exceptions import DivisionByZeroError
from app.operations import Add, Subtract, Multiply, Divide, Power, Root


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

def test_factory_returns_all_operations():
    ops = ["add", "subtract", "multiply", "divide", "power", "root"]

    for op in ops:
        assert OperationFactory.get_operation(op) is not None

def test_operation_abstract_class_exists():
    assert Operation.__name__ == "Operation"

def test_all_operation_classes_directly():
    assert Add().execute(1, 1) == 2
    assert Subtract().execute(2, 1) == 1
    assert Multiply().execute(2, 2) == 4
    assert Divide().execute(4, 2) == 2
    assert Power().execute(2, 3) == 8
    assert Root().execute(9, 2) == 3

def test_operation_abstract_class_behavior():
    with pytest.raises(TypeError):
        Operation()   # cannot instantiate ABC properly

def test_operation_execute_is_abstract():
    op = Operation.__abstractmethods__
    assert "execute" in op

def test_operation_abstract_method_is_unreachable():
    from app.operations import Operation
    assert Operation.execute is not None

def test_operation_execute_base_body():
    class ConcreteOperation(Operation):
        def execute(self, a, b):
            return super().execute(a, b)

    assert ConcreteOperation().execute(1, 2) is None
