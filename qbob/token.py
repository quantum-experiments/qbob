"""Define a representation of a typed token in Q# code."""

from qbob.types import to_qsharp_value
from typing import Union, List

class Token:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        self.is_adj = False
        self.is_ctl = False

    def __getitem__(self, key: int) -> 'Token':
        assert self.type.endswith("[]"), self.type
        return Token(f"{self}[{key}]", self.type[:-2])

    def __eq__(self, value: object) -> 'Token':
        return Token(f"{self} == {to_qsharp_value(value)}", "Bool")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Token({repr(self.name)}, {repr(self.type)})"

    def set_adj(self, b: bool) -> 'Token':
        self.isAdj = b
        return self

    def set_ctl(self, b: bool) -> 'Token':
        self.is_ctl = b
        return self

    def update_name(self, new_name):
        self.name = new_name


    """control: can be a single Token of type Qubit or an array of Tokens of type Qubit[]"""
    def controlled_on(self, control) -> 'Token':
        def tokens_to_str(control: Union[List, Token]) -> str:
            if isinstance(control, list):
                return ",".join([c.name for c in control])
            return control.name

        assert self.is_ctl == True
        gate = self.name[0 : self.name.find("(")]
        old_input = self.name[self.name.find("(") + 1 : -1]

        if (gate == "SWAP"):
            new_input = f"[{tokens_to_str(control)}], ({old_input})"

        elif (gate == "CNOT"):
            assert not isinstance(control, list)
            new_input = f"{control.name}, {old_input}"
            return Token(f"C{gate}({new_input})", "Unit")

        else:
            new_input = f"[{tokens_to_str(control)}], {old_input}"

        return Token(f"Controlled {gate}({new_input})", "Unit")


    """`bits` and `qubits` can both be a single Token or an array of Tokens of the appropriate type"""
    def controlled_on_bit_string(self, bits, qubits) -> 'Token':
        def qubits_to_str(qubit_list: Union[List, Token]) -> str:
            if isinstance(qubit_list, list):
                return ",".join([q.name for q in qubit_list])
            return qubit_list.name

        def bits_to_str(bit_list):
            if isinstance(bit_list, list):
                return ",".join([("true" if b else "false") for b in bit_list])
            return "true" if bit_list else "false"

        assert self.is_ctl == True
        gate = self.name[0 : self.name.find("(")]
        old_input = self.name[self.name.find("(") + 1 : -1]

        if (isinstance(qubits, Token) and qubits.type == "Qubit[]"):
            qubit_control = qubits.name
        else:
            qubit_control = f"[{qubits_to_str(qubits)}]"

        if (isinstance(bits, Token) and bits.type == "Bool[]"):
            bit_control = bits.name
        else:
            bit_control = f"[{bits_to_str(bits)}]"

        return Token(f"ApplyControlledOnBitString({bit_control}, {gate}, {qubit_control}, {old_input})", "Unit")
