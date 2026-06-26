# Unit Testing Documentation

## Testing Framework
We use pytest for all unit and integration testing.

---

## Test Coverage Goals
- 100% line coverage (required by CI)
- Edge case validation
- Exception handling verification

---

## Test Categories

### 1. Unit Tests
- operations.py
- calculation.py
- input_validators.py

### 2. Integration Tests
- calculator_repl.py
- history.py
- memento system

### 3. System Tests
- full command execution flow
- REPL input simulation

---

## Example Test Command
```bash
pytest --cov=app