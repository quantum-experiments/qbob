#!/usr/bin/env python

"""Tests for `qbob` package.""" 

import pytest
from typing import List

import qsharp
from qbob import qbob
from qbob import intrinsics
from qbob.types import *


def without_whitespace(string):
    return "".join(string.split())

def test_empty_operation():
    my_qbob = qbob.OperationBuilder("DoNothing")

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace("operation DoNothing() : Unit { }")
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

def test_adjoint_operation():
    my_qbob = qbob.OperationBuilder("DoNothingAdjoint")
    my_qbob.is_adj = True

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace("operation DoNothingAdjoint() : Unit is Adj { }")
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

def test_control_operation():
    my_qbob = qbob.OperationBuilder("DoNothingControl")
    my_qbob.is_ctl = True

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace("operation DoNothingControl() : Unit is Ctl { }")
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

def test_adjoint_and_control_operation():
    my_qbob = qbob.OperationBuilder("DoNothingAdjointControl")
    my_qbob.is_adj = True
    my_qbob.is_ctl = True

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace("operation DoNothingAdjointControl() : Unit is Adj+Ctl { }")
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

def test_empty_operation_with_input():
    my_qbob = qbob.OperationBuilder("DoNothingWithInput")
    my_qbob.input("q", List[Qubit])
    
    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace("operation DoNothingWithInput(q : Qubit[]) : Unit { }")
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

def test_empty_operation_with_multiple_input():
    my_qbob = qbob.OperationBuilder("DoNothingWithMultipleInput")
    my_qbob.input("q", List[Qubit])
    my_qbob.input("i", int)
    
    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace("operation DoNothingWithMultipleInput(q : Qubit[], i: Int) : Unit { }")
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()
    
def test_single_gate():
    my_qbob = qbob.OperationBuilder("SingleGate")
    qubits = my_qbob.input("q", List[Qubit])
    
    my_qbob += intrinsics.H(qubits[0])
    
    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace("operation SingleGate(q : Qubit[]) : Unit { H(q[0]); }")
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

def test_two_gates():
    my_qbob = qbob.OperationBuilder("TwoGates")
    qubits = my_qbob.input("q", List[Qubit])
    
    my_qbob += intrinsics.H(qubits[0])
    my_qbob += intrinsics.CNOT(qubits[0], qubits[1])
    
    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace("operation TwoGates(q : Qubit[]) : Unit { H(q[0]); CNOT(q[0], q[1]); }")
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

def test_allocate_qubit(allocate_qubit):
    my_qbob = qbob.OperationBuilder("AllocateQubit")
    with my_qbob.allocate_qubits("q", 1) as q:
        my_qbob += intrinsics.Z(q)

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace(allocate_qubit)
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

def test_allocate_two_qubits(allocate_two_qubits):
    my_qbob = qbob.OperationBuilder("AllocateTwoQubits")
    with my_qbob.allocate_qubits("q", 2) as q:
        my_qbob += intrinsics.Z(q[0])
        my_qbob += intrinsics.Z(q[1])

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace(allocate_two_qubits)
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()


def test_measure_entangled_state(measure_entangled_state):
    my_qbob = qbob.OperationBuilder("MeasureEntangledState")
    with my_qbob.allocate_qubits("qubits", 2) as q:
        my_qbob += intrinsics.H(q[0])
        my_qbob += intrinsics.CNOT(q[0], q[1])
        my_qbob.returns([intrinsics.M(q[0]), intrinsics.M(q[1])])

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace(measure_entangled_state)
            == without_whitespace(qsharp_code))
