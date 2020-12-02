"""Define functions representing intrinsic Q# operations."""

from qbob.qbob import Token

def H(qubit: Token) -> Token:
    return Token(f"H({qubit.name})", "Unit")

def M(qubit: Token) -> Token:
    return Token(f"M({qubit.name})", "Result")
    
def Z(qubit: Token) -> Token:
    return Token(f"Z({qubit.name})", "Unit")

def CNOT(source_qubit: Token,
         target_qubit: Token) -> Token:
    return Token(f"CNOT({source_qubit.name}, {target_qubit.name})", "Unit")
