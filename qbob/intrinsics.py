"""Define functions representing intrinsic Q# operations."""

from qbob.qbob import Token

def H(qubit: Token) -> Token:
    return Token(f"H({qubit})", "Unit").set_ctl(True).set_adj(True)

def M(qubit: Token) -> Token:
    return Token(f"M({qubit})", "Result")

def Measure(bases: list, qubits: object) -> Token:
    assert isinstance (bases, list)
    if isinstance(qubits, list):
        return Token(f"Measure([{','.join(f'{n.name}' for n in bases)}], "
            + f"[{','.join(f'{q.name}' for q in qubits)}])", "Result")

    if isinstance(qubits, Token):
        assert (qubits.type == "Qubit[]")
        return Token(f"Measure([{','.join(f'{n.name}' for n in bases)}], {qubits.name})", "Result")

def Reset(qubit: Token) -> Token:
    return Token(f"Reset({qubit})", "Unit")
    
def X(qubit: Token) -> Token:
    return Token(f"X({qubit})", "Unit").set_ctl(True).set_adj(True)

def Y(qubit: Token) -> Token:
    return Token(f"Y({qubit})", "Unit").set_ctl(True).set_adj(True)
    
def Z(qubit: Token) -> Token:
    return Token(f"Z({qubit})", "Unit").set_ctl(True).set_adj(True)

def CNOT(source_qubit: Token, target_qubit: Token) -> Token:
    return Token(f"CNOT({source_qubit}, {target_qubit})", "Unit").set_ctl(True).set_adj(True)

def SWAP(qubit1: Token, qubit2: Token) -> Token:
    return Token(f"SWAP({qubit1}, {qubit2})", "Unit").set_ctl(True).set_adj(True)

def Message(s: str) -> Token:
    return Token(f"Message(\"{s}\")", "Unit")
