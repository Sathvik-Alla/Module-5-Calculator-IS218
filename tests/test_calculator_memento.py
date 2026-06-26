from app.calculator_memento import CalculatorMemento
from app.calculation import Calculation


def test_memento_save_and_undo():
    m = CalculatorMemento()
    c1 = Calculation("add", 1, 2, 3)

    m.save(c1)
    state = m.undo()

    assert state == c1


def test_redo():
    m = CalculatorMemento()
    c1 = Calculation("add", 1, 2, 3)

    m.save(c1)
    m.undo()
    state = m.redo()

    assert state == c1


def test_empty_undo():
    m = CalculatorMemento()
    assert m.undo() is None


def test_empty_redo():
    m = CalculatorMemento()
    assert m.redo() is None