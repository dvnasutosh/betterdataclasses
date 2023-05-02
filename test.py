from StrictDictionary import StrictDictionary

from typing import List

class SD(StrictDictionary):
    a: int
    b: int
    c: str

class NestedSD(StrictDictionary):
    name: str
    values: List[SD]

class ComplexSD(StrictDictionary):
    x: float
    y: float
    nested: NestedSD

print(ComplexSD().__raw__())