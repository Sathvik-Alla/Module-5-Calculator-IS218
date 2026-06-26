class Memento:
    def __init__(self, state):
        self.state = state


class CalculatorMemento:
    """Undo/Redo system"""

    def __init__(self):
        self.history = []
        self.future = []

    def save(self, state):
        self.history.append(Memento(state))
        self.future.clear()

    def undo(self):
        if not self.history:
            return None

        memento = self.history.pop()
        self.future.append(memento)
        return memento.state

    def redo(self):
        if not self.future:
            return None

        memento = self.future.pop()
        self.history.append(memento)
        return memento.state