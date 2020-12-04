"""Define the OperationBuilder class."""

from contextlib import contextmanager
from typing import List, Union, _GenericAlias

from qbob.token import Token
from qbob.types import to_qsharp_type
from qbob.formatter import QSharpFormatter


NEWLINE = "\n"


class OperationBuilder:

    _OPERATION_TEMPLATE = \
        """{attributes} operation {name} ( {arguments} ) : {return_type} {characteristics}
        {{
            {statements}
        }}"""

    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.input_parameters = {}
        self.is_adj = False
        self.is_ctl = False
        self.is_entrypoint = False

        self.statements = []
        self.return_type = "Unit"

    @property
    def attributes(self) -> str:
        return "@EntryPoint()" if self.is_entrypoint else ""

    @property
    def arguments(self) -> str:
        return ",".join(
            [
                f"{n} : {to_qsharp_type(t)}" for n, t in self.input_parameters.items()
            ]
        )

    @property
    def characteristics(self) -> str:
        chars = ("is Adj + Ctl" if self.is_adj and self.is_ctl
                else "is Adj" if self.is_adj
                else "is Ctl" if self.is_ctl
                else "")
        return chars

    @property
    def op_statements(self) -> str:
        return NEWLINE.join(self.statements)

    def to_str(self) -> str:
        return self._OPERATION_TEMPLATE.format(
            name=self.operation_name,
            attributes=self.attributes,
            arguments=self.arguments,
            return_type=self.return_type,
            characteristics=self.characteristics,
            statements=self.op_statements
        )

    def build(self) -> str:
        """Generate formatted Q# code from the builder

        :return: Formatted Q# code
        :rtype: str
        """
        formatter = QSharpFormatter()
        unformatted_code = self.to_str()
        return formatter.format_input(unformatted_code)

    def __call__(self, *args) -> Token:
        assert len(args) == len(self.input_parameters)
        args_as_str = [str(arg) for arg in args]
        return Token(f"{self.operation_name}({','.join(args_as_str)})", self.return_type)

    def input(self, parameter_name: str, parameter_type: Union[type, _GenericAlias]) -> Token:
        assert isinstance(parameter_name, str)
        assert (isinstance(parameter_type, type)
                or isinstance(parameter_type, _GenericAlias))
        self.input_parameters[parameter_name] = parameter_type

        return Token(parameter_name, to_qsharp_type(parameter_type))

    def add_local(self, name: str, value: object, immutable: bool = False) -> Token:
        self.statements.append(f"{'let' if immutable else 'mutable'} {name} = {value};")
        return Token(name, to_qsharp_type(type(value)))

    def set_local(self, local: Token, value: object) -> None:
        self.statements.append(f"set {local} = {value};")

    def returns(self, *return_tokens) -> None:
        def to_qsharp_return_value(return_token: Union[List, Token]) -> str:
            if isinstance(return_token, list):
                return "[" + ",".join([to_qsharp_return_value(token) for token in return_token]) + "]"
            return return_token.name
        
        def to_qsharp_return_type(return_token: Union[List, Token]) -> str:
            if isinstance(return_token, list):
                return f"{to_qsharp_return_type(return_token[0])}[]"
            return return_token.type

        ret_val = ','.join([to_qsharp_return_value(r) for r in return_tokens])
        self.statements.append(f"return {ret_val};")

        self.return_type = ','.join([to_qsharp_return_type(r) for r in return_tokens])
        
    @contextmanager
    def allocate_qubits(self, register_name: str, num_qubits: Union[int, Token]):
        assert isinstance(num_qubits, Token) or num_qubits > 0

        if isinstance(num_qubits, int) and num_qubits == 1:
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
            self.statements.append(f"until ({condition})")
            if fixup:
                self.statements.append("fixup {")
                for expression in fixup:
                    self += expression
                self.statements.append("}")

    @contextmanager
    def if_statement(self, condition: Token):
        assert condition.type == "Bool"
        self.statements.append(f"if ({condition}) {{")
        try:
            yield
        finally:
            self.statements.append("}")

    def __iadd__(self, expression: Token) -> 'OperationBuilder':
        self.statements.append(f"{expression};")
        return self
