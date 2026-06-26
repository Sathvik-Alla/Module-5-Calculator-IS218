import builtins
from app.calculator_repl import CalculatorREPL


def test_repl_help(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl = CalculatorREPL()
    repl.run()

    captured = capsys.readouterr()
    assert "Commands" in captured.out


def test_repl_add(monkeypatch, capsys):
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl = CalculatorREPL()
    repl.run()

    captured = capsys.readouterr()
    assert "Result" in captured.out