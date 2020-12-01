"""Main module."""

from contextlib import contextmanager
from typing import List, Union, _GenericAlias

from qbob.types import _to_qsharp_type


class Token:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def __getitem__(self, key: int) -> 'Token':
        assert self.type.endswith("[]")
        return Token(f"{self.name}[{key}]", self.type[:-2])

class OperationBuilder:

    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.input_parameters = {}
        self.is_adj = False
        self.is_ctl = False

        self.statements = []
        self.return_type = "Unit"

    def to_str(self) -> str:
        return (
            f"operation {self.operation_name}("
            + ",".join([f"{n} : {_to_qsharp_type(t)}"
                        for n,t in self.input_parameters.items()])
            + f") : {self.return_type} "
            + ("is Adj+Ctl" if self.is_adj and self.is_ctl
                else "is Adj" if self.is_adj
                else "is Ctl" if self.is_ctl
                else "")
            + " {"
            + "\n".join(self.statements)
            + "}"
        )

    def input(self, parameter_name: str, parameter_type: Union[type, _GenericAlias]):
        assert isinstance(parameter_name, str)
        assert (isinstance(parameter_type, type)
                or isinstance(parameter_type, _GenericAlias))
        self.input_parameters[parameter_name] = parameter_type

        return Token(parameter_name, _to_qsharp_type(parameter_type))


    def returns(self, *return_tokens):
        def to_qsharp_return_value(obj):
            if isinstance(obj, list):
                return "[" + ",".join([o.name for o in obj]) + "]"
            return obj.name
        
        def to_qsharp_return_type(obj):
            if isinstance(obj, list):
                return f"{obj[0].type}[]"
            return obj.type

        ret_val = ','.join([to_qsharp_return_value(r) for r in return_tokens])
        self.statements.append(f"return {ret_val};")

        self.return_type = ','.join([to_qsharp_return_type(r) for r in return_tokens])
        
    @contextmanager
    def allocate_qubits(self, register_name: str, num_qubits: int):
        assert num_qubits > 0
        if num_qubits == 1:
            self.statements.append(f"using ({register_name} = Qubit())")
            type_name = "Qubit"
        else:
            self.statements.append(f"using ({register_name} = Qubit[{num_qubits}])")
            type_name = "Qubit[]"
        
        self.statements.append("{")
        try:
            yield Token(register_name, type_name)
        finally:
            self.statements.append("}")

    def __iadd__(self, other) -> 'OperationBuilder':
        self.statements.append(f"{other.name};")
        return self
