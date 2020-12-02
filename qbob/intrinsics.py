"""Define functions representing intrinsic Q# operations."""

from qbob.qbob import Token

def H(qubit: Token) -> Token:
    return Token(f"H({qubit})", "Unit")

def M(qubit: Token) -> Token:
    return Token(f"M({qubit})", "Result")

def Reset(qubit: Token) -> Token:
    return Token(f"Reset({qubit})", "Unit")
    
def X(qubit: Token) -> Token:
    return Token(f"X({qubit})", "Unit")
    
def Y(qubit: Token) -> Token:
    return Token(f"Y({qubit})", "Unit")
    
def Z(qubit: Token) -> Token:
    return Token(f"Z({qubit})", "Unit")

def CNOT(source_qubit: Token, target_qubit: Token) -> Token:
    return Token(f"CNOT({source_qubit}, {target_qubit})", "Unit")
