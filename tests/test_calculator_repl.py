import builtins
import runpy
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
    assert "5.0" in captured.out

    
def test_repl_all_commands(monkeypatch, capsys):
    inputs = iter([
        "history",
        "clear",
        "save",
        "load",
        "undo",
        "redo",
        "exit"
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl = CalculatorREPL()
    repl.run()

    out = capsys.readouterr().out
    assert "History" in out or "Saved" in out or "Loaded" in out

def test_repl_full_branch_coverage(monkeypatch, capsys):
    inputs = iter([
        "add 2 3",
        "invalidcommand",
        "divide 10 0",
        "undo",
        "redo",
        "save",
        "load",
        "history",
        "clear",
        "exit"
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl = CalculatorREPL()
    repl.run()

    out = capsys.readouterr().out

    assert "Result" in out
    assert "Error" in out

def test_repl_invalid_command(monkeypatch, capsys):
    inputs = iter(["badcommand 1 2", "exit"])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl = CalculatorREPL()
    repl.run()

    out = capsys.readouterr().out

    assert "Unexpected error" in out or "Error" in out

def test_repl_unexpected_error(monkeypatch, capsys):
    inputs = iter(["add two three", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl = CalculatorREPL()
    repl.run()

    out = capsys.readouterr().out

    assert "Unexpected error" in out or "Error" in out

def test_repl_force_generic_exception(monkeypatch, capsys):
    import builtins
    from app.calculator_repl import CalculatorREPL

    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # force unexpected exception at runtime
    def crash(*args, **kwargs):
        raise Exception("boom")

    import app.calculator_repl as calculator_repl
    monkeypatch.setattr(calculator_repl, "validate_args", crash)

    repl = CalculatorREPL()
    repl.run()

    out = capsys.readouterr().out
    assert "Unexpected error" in out or "Error" in out

def test_repl_main_entry_point(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    runpy.run_module("app.calculator_repl", run_name="__main__")

    out = capsys.readouterr().out
    assert "Calculator REPL started" in out
