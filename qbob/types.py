"""Define mappings between Python types and Q# types."""

from typing import List, Union, _GenericAlias

def to_qsharp_type(python_type: type) -> str:
    if python_type == List[Qubit]:
        return "Qubit[]"
    elif python_type == List[Result]:
        return "Result[]"
    elif python_type == Qubit:
        return "Qubit"
    elif python_type == Result:
        return "Result"
    elif python_type == bool:
        return "Bool"
    elif python_type == int:
        return "Int"
    elif python_type == str:
        return "String"
    
    return None

class Qubit:
    pass

class Result:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value

Zero = Result("Zero")
One = Result("One")
