from dataclasses import dataclass


@dataclass
class Calculation:
    operation: str
    a: float
    b: float
    result: float