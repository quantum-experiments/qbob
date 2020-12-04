"""Diagnostics library"""

from typing import List, Union, _GenericAlias

from qbob.qbob import Token
from qbob.types import to_qsharp_escaped_string


def DumpMachine(file_location: str) -> Token:
    return Token(f"Microsoft.Quantum.Diagnostics.DumpMachine(\"{to_qsharp_escaped_string(file_location)}\")", "Unit")


def DumpRegister(file_location: str, qubits: Union[Token, List[Token]]) -> Token:
    # qbob += DumpRegister("filename", [q])
    # -->
    # DumpRegister("filename", [q])
    if isinstance(qubits, Token) and qubits.type == "Qubit":
        qubits = Token(f"[{qubits}]", f"Qubit[]")
    elif isinstance(qubits, list):
        qubits = Token(f"[{','.join([q.name for q in qubits])}]", f"{qubits[0].type}[]")
    return Token(f"Microsoft.Quantum.Diagnostics.DumpRegister(\"{to_qsharp_escaped_string(file_location)}\", {qubits})", "Unit")
