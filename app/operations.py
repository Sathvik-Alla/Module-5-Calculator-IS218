from abc import ABC, abstractmethod
from app.exceptions import DivisionByZeroError


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        return a ** (1 / b)


class OperationFactory:
    """Factory Pattern"""

    @staticmethod
    def get_operation(name):
        operations = {
            "add": Add(),
            "subtract": Subtract(),
            "multiply": Multiply(),
            "divide": Divide(),
            "power": Power(),
            "root": Root(),
        }

        if name not in operations:
            raise ValueError(f"Unknown operation: {name}")

        return operations[name]