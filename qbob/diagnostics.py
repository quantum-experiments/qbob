"""Diagnostics library"""

from typing import List, Union, _GenericAlias

from qbob.qbob import Token


def DumpMachine(file_location: str) -> Token:
    return Token(f"Microsoft.Quantum.Diagnostics.DumpMachine(\"{file_location}\")", "Unit")


def DumpRegister(file_location: str, qubits: Union[Token, List[Token]]) -> Token:
    # qbob += DumpRegister("filename", [q])
    # -->
    # DumpRegister("filename", [q])
    if isinstance(qubits, Token) and qubits.type == "Qubit":
        qubits = Token(f"[{qubits}]", f"Qubit[]")
    elif isinstance(qubits, list):
        qubits = Token(f"[{','.join([q.name for q in qubits])}]", f"{qubits[0].type}[]")
    return Token(f"Microsoft.Quantum.Diagnostics.DumpRegister(\"{file_location}\", {qubits})", "Unit")
