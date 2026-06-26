from app.operations import OperationFactory
from app.input_validators import validate_args
from app.calculation import Calculation
from app.history import History
from app.calculator_memento import CalculatorMemento
from app.calculator_config import CalculatorConfig
from app.exceptions import CalculatorError


class CalculatorREPL:
    def __init__(self):
        self.history = History()
        self.memento = CalculatorMemento()
        self.config = CalculatorConfig()

    def run(self):
        print("Calculator REPL started. Type 'help'.")

        while True:
            user_input = input(">>> ").strip().lower()

            if user_input == "exit":
                break

            if user_input == "help":
                print("Commands: add, subtract, multiply, divide, power, root, history, save, load, undo, redo, clear, exit")
                continue

            if user_input == "history":
                print(self.history.show())
                continue

            if user_input == "clear":
                self.history.clear()
                print("History cleared")
                continue

            if user_input == "save":
                self.history.save(self.config.history_file)
                print("Saved")
                continue

            if user_input == "load":
                self.history.load(self.config.history_file)
                print("Loaded")
                continue

            if user_input == "undo":
                state = self.memento.undo()
                print("Undo:", state)
                continue

            if user_input == "redo":
                state = self.memento.redo()
                print("Redo:", state)
                continue

            try:
                parts = user_input.split()
                op_name = parts[0]
                a, b = validate_args(parts[1:])

                operation = OperationFactory.get_operation(op_name)
                result = operation.execute(a, b)

                calc = Calculation(op_name, a, b, result)

                self.history.add(calc)
                self.memento.save(calc)

                print("Result:", result)

            except CalculatorError as e:
                print("Error:", e)
            except Exception as e:
                print("Unexpected error:", e)


if __name__ == "__main__":
    CalculatorREPL().run()