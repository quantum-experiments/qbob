"""Define mappings between Python types and Q# types."""

from typing import List, Union, _GenericAlias

def _to_qsharp_type(python_type: type) -> str:
    if python_type == List[Qubit]:
        return "Qubit[]"
    elif python_type == int:
        return "Int"
    elif python_type == str:
        return "String"
    
    return None

class Qubit:
    pass