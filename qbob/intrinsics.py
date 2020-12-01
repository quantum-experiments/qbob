"""Define functions representing intrinsic Q# operations."""

from qbob.qbob import InputParameter

def H(qubit: InputParameter) -> str:
    return f"H({qubit.name});"

def CNOT(
        source_qubit: InputParameter,
        target_qubit: InputParameter) -> str:
    return f"CNOT({source_qubit.name}, {target_qubit.name});"
