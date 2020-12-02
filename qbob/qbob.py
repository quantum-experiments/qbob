"""Main module."""

from contextlib import contextmanager
from typing import List, Union, _GenericAlias

from qbob.token import Token
from qbob.types import to_qsharp_type


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
            + ",".join([f"{n} : {to_qsharp_type(t)}"
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

    def input(self, parameter_name: str, parameter_type: Union[type, _GenericAlias]) -> Token:
        assert isinstance(parameter_name, str)
        assert (isinstance(parameter_type, type)
                or isinstance(parameter_type, _GenericAlias))
        self.input_parameters[parameter_name] = parameter_type

        return Token(parameter_name, to_qsharp_type(parameter_type))

    def add_local(self, name: str, value: object, immutable: bool = False) -> Token:
        if isinstance(value, Token):
            value = value.name
        self.statements.append(f"{'let' if immutable else 'mutable'} {name} = {value};")
        return Token(name, to_qsharp_type(type(value)))

    def set_local(self, local: Token, value: object) -> None:
        if isinstance(value, Token):
            value = value.name
        self.statements.append(f"set {local.name} = {value};")

    def returns(self, *return_tokens) -> None:
        def to_qsharp_return_value(obj):
            if isinstance(obj, list):
                return "[" + ",".join([to_qsharp_return_value(o) for o in obj]) + "]"
            return obj.name
        
        def to_qsharp_return_type(obj):
            if isinstance(obj, list):
                return f"{to_qsharp_return_type(obj[0])}[]"
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

    @contextmanager
    def within(self, expressions: Union[Token, List[Token]]):
        if not isinstance(expressions, list):
            expressions = [expressions]
        
        self.statements.append("within {")
        for expression in expressions:
            self += expression
        self.statements.append("} apply {")
        try:
            yield
        finally:
            self.statements.append("}")
    
    @contextmanager
    def repeat_until(self, condition: Token, fixup: Union[Token, List[Token]] = []):
        assert condition.type == to_qsharp_type(bool)
        if not isinstance(fixup, list):
            fixup = [fixup]
        
        self.statements.append("repeat {")
        try:
            yield
        finally:
            self.statements.append("}")
            self.statements.append(f"until ({condition.name})")
            if fixup:
                self.statements.append("fixup {")
                for expression in fixup:
                    self += expression
                self.statements.append("}")

    def __iadd__(self, expression: Token) -> 'OperationBuilder':
        self.statements.append(f"{expression.name};")
        return self
