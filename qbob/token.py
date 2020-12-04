"""Define a representation of a typed token in Q# code."""

from qbob.types import to_qsharp_value

class Token:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def __getitem__(self, key: int) -> 'Token':
        assert self.type.endswith("[]"), self.type
        return Token(f"{self}[{key}]", self.type[:-2])

    def __eq__(self, value: object) -> 'Token':
        return Token(f"{self} == {to_qsharp_value(value)}", "Bool")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Token({repr(self.name)}, {repr(self.type)})"
