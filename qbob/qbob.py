"""Main module."""

from typing import List, Union, _GenericAlias

from qbob.types import _to_qsharp_type


class InputParameter:
    def __init__(self, name: str):
        self.name = name

    def __getitem__(self, key: int) -> 'InputParameter':
        return InputParameter(f"{self.name}[{key}]")

class OperationBuilder:

    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.input_parameters = {}
        self.is_adj = False
        self.is_ctl = False

        self.statements = []

    def to_str(self) -> str:
        return (
            f"operation {self.operation_name}("
            + ",".join([f"{n} : {_to_qsharp_type(t)}"
                        for n,t in self.input_parameters.items()])
            + ") : Unit "
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

        return InputParameter(parameter_name)

    def __iadd__(self, other) -> 'OperationBuilder':
        self.statements.append(other)
        return self
