import os
from app.calculator_config import CalculatorConfig


def test_config_defaults():
    config = CalculatorConfig()
    assert isinstance(config.history_file, str)


def test_config_env(monkeypatch):
    monkeypatch.setenv("DEBUG", "True")
    monkeypatch.setenv("HISTORY_FILE", "test.csv")

    config = CalculatorConfig()
    assert config.debug is True
    assert config.history_file == "test.csv"