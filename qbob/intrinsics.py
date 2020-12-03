"""Define functions representing intrinsic Q# operations."""

from qbob.qbob import Token

def H(qubit: Token) -> Token:
    return Token(f"H({qubit.name})", "Unit")

def M(qubit: Token) -> Token:
    return Token(f"M({qubit.name})", "Result")

def Measure(bases, qubits: Token) -> Token:
    return Token(f"Measure([{','.join(f'{n.name}' for n in bases)}], "
        + f"[{','.join(f'{q.name}' for q in qubits)}])", "Result")

def Reset(qubit: Token) -> Token:
    return Token(f"Reset({qubit.name})", "Unit")
    
def X(qubit: Token) -> Token:
    return Token(f"X({qubit.name})", "Unit")
    
def Y(qubit: Token) -> Token:
    return Token(f"Y({qubit.name})", "Unit")
    
def Z(qubit: Token) -> Token:
    return Token(f"Z({qubit.name})", "Unit")

def CNOT(source_qubit: Token,
         target_qubit: Token) -> Token:
    return Token(f"CNOT({source_qubit.name}, {target_qubit.name})", "Unit")

def print(s: str) -> Token:
    return Token(f"Message(\"{s}\")", "Unit")
