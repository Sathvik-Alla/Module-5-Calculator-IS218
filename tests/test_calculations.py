from app.calculation import Calculation

def test_calculation_dataclass():
    c = Calculation("add", 2, 3, 5)
    assert c.operation == "add"
    assert c.a == 2
    assert c.b == 3
    assert c.result == 5