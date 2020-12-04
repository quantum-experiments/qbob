#!/usr/bin/env python

"""Tests for `qbob` package.""" 

import pytest
from typing import List

from qbob import qbob
from qbob.intrinsics import *
from qbob.types import *


def test_empty_operation(noop):
    my_qbob = qbob.OperationBuilder("DoNothing")

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert noop == qsharp_code


def test_adjoint_operation(noop_adj):
    my_qbob = qbob.OperationBuilder("DoNothingAdjoint")
    my_qbob.is_adj = True

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert noop_adj == qsharp_code


def test_control_operation(noop_ctl):
    my_qbob = qbob.OperationBuilder("DoNothingControl")
    my_qbob.is_ctl = True

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert noop_ctl == qsharp_code


def test_adjoint_and_control_operation(noop_adj_ctl):
    my_qbob = qbob.OperationBuilder("DoNothingAdjointControl")
    my_qbob.is_adj = True
    my_qbob.is_ctl = True

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert noop_adj_ctl == qsharp_code


def test_empty_operation_with_input(noop_input):
    my_qbob = qbob.OperationBuilder("DoNothingWithInput")
    my_qbob.input("q", List[Qubit])
    
    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert noop_input == qsharp_code


def test_empty_operation_with_multiple_input(noop_two_input):
    my_qbob = qbob.OperationBuilder("DoNothingWithMultipleInput")
    my_qbob.input("q", List[Qubit])
    my_qbob.input("i", int)
    
    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert noop_two_input == qsharp_code


def test_single_gate(single_gate):
    my_qbob = qbob.OperationBuilder("SingleGate")
    qubits = my_qbob.input("q", List[Qubit])
    
    my_qbob += H(qubits[0])
    
    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert single_gate == qsharp_code


def test_two_gates(two_gates):
    my_qbob = qbob.OperationBuilder("TwoGates")
    qubits = my_qbob.input("q", List[Qubit])
    
    my_qbob += H(qubits[0])
    my_qbob += CNOT(qubits[0], qubits[1])
    
    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert two_gates == qsharp_code


def test_allocate_qubit(allocate_qubit):
    my_qbob = qbob.OperationBuilder("AllocateQubit")
    with my_qbob.allocate_qubits("q", 1) as q:
        my_qbob += Z(q)

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert allocate_qubit == qsharp_code


def test_allocate_two_qubits(allocate_two_qubits):
    my_qbob = qbob.OperationBuilder("AllocateTwoQubits")
    with my_qbob.allocate_qubits("q", 2) as q:
        my_qbob += Z(q[0])
        my_qbob += Z(q[1])

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert allocate_two_qubits == qsharp_code


def test_measure_entangled_state(measure_entangled_state):
    my_qbob = qbob.OperationBuilder("MeasureEntangledState")
    with my_qbob.allocate_qubits("qubits", 2) as q:
        my_qbob += H(q[0])
        my_qbob += CNOT(q[0], q[1])
        my_qbob.returns([M(q[0]), M(q[1])])

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert measure_entangled_state == qsharp_code


def test_within_apply(h_x_h):
    my_qbob = qbob.OperationBuilder("HXH")
    with my_qbob.allocate_qubits("q", 1) as q:
        with my_qbob.within(H(q)):
            my_qbob += X(q)

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert h_x_h == qsharp_code


def test_measure_until_one(measure_until_one):
    my_qbob = qbob.OperationBuilder("MeasureUntilOne")
    with my_qbob.allocate_qubits("q", 1) as q:
        result = my_qbob.add_local("result", Zero)
        with my_qbob.repeat_until(result == One,
                fixup = Reset(q)):
            my_qbob += H(q)
            my_qbob.set_local(result, M(q))

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert measure_until_one == qsharp_code


def test_hello_world(hello_world):
    my_qbob = qbob.OperationBuilder("HelloWorld")
    my_qbob += Message("Hello World!")

    qsharp_code = my_qbob.build()
    assert hello_world == qsharp_code


def test_hello_world_qubit(hello_world_qubit):
    my_qbob = qbob.OperationBuilder("HelloWorlds")
    qubits = my_qbob.input("register", List[Qubit])

    my_qbob += H(qubits[0])
    my_qbob += H(qubits[1])

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert hello_world_qubit == qsharp_code


def test_prepare_entangled_state(prepare_entangled_state):
    my_qbob = qbob.OperationBuilder("PrepareEntangledState")
    my_qbob.is_adj = True
    qubits = my_qbob.input("qubits", List[Qubit])

    my_qbob += H(qubits[0])
    my_qbob += CNOT(qubits[0], qubits[1])

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert prepare_entangled_state == qsharp_code


def test_is_plus(is_plus):
    my_qbob = qbob.OperationBuilder("IsPlus")
    q = my_qbob.input("q", Qubit)
    my_qbob.returns(Measure([Pauli.PauliX], [q]) == Zero)

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert is_plus == qsharp_code


def test_is_minus(is_minus):
    my_qbob = qbob.OperationBuilder("IsMinus")
    q = my_qbob.input("q", Qubit)
    my_qbob.returns(Measure([Pauli.PauliX], [q]) == One)

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert is_minus == qsharp_code


def test_teleport(teleport):
    my_qbob = qbob.OperationBuilder("Teleport")
    msg = my_qbob.input("msg", Qubit)
    target = my_qbob.input("target", Qubit)
    with my_qbob.allocate_qubits("auxiliary", 1) as aux:
        my_qbob += H(aux)
        my_qbob += CNOT(aux, target)
        my_qbob += CNOT(msg, aux)
        my_qbob += H(msg)
        with my_qbob.if_statement(Measure([Pauli.PauliZ], [msg]) == One):
            my_qbob += Z(target)
        with my_qbob.if_statement(Measure([Pauli.PauliZ], [aux]) == One):
            my_qbob += X(target)

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert teleport == qsharp_code


def test_nested_operations(prepare_entangled_state, measure_entangled_state_using_prepare):
    prepare_qbob = qbob.OperationBuilder("PrepareEntangledState")
    prepare_qbob.is_adj = True
    qubits = prepare_qbob.input("qubits", List[Qubit])
    prepare_qbob += H(qubits[0])
    prepare_qbob += CNOT(qubits[0], qubits[1])

    qsharp_code = prepare_qbob.build()
    print(qsharp_code)
    assert prepare_entangled_state == qsharp_code

    measure_qbob = qbob.OperationBuilder("MeasureEntangledState")
    with measure_qbob.allocate_qubits("qubits", 2) as q:
        measure_qbob += prepare_qbob(q)
        measure_qbob.returns([M(q[0]), M(q[1])])

    qsharp_code = measure_qbob.build()
    print(qsharp_code)
    assert measure_entangled_state_using_prepare == qsharp_code


def test_empty_entrypoint(with_entrypoint):
    my_qbob = qbob.OperationBuilder("RunProgram")
    my_qbob.is_entrypoint = True
    num_qubits = my_qbob.input("nQubits", int)
    with my_qbob.allocate_qubits("register", num_qubits) as q:
        my_qbob += H(q[0])

    qsharp_code = my_qbob.build()
    print(qsharp_code)
    assert with_entrypoint == qsharp_code


def test_measure_array(measure_array):
    my_qbob = qbob.OperationBuilder("MeasureArray")
    qubits = my_qbob.input("qubits", List[Qubit])
    measure = Measure([Pauli.PauliZ, Pauli.PauliZ], qubits)
    my_qbob.add_local("result", measure, True)

    qsharp_code = my_qbob.formatted()
    print(qsharp_code)
    assert measure_array == qsharp_code


def test_measure_array_items(measure_array_items):
    my_qbob = qbob.OperationBuilder("MeasureArrayItems")
    qubits = my_qbob.input("qubits", List[Qubit])
    measure = Measure([Pauli.PauliZ, Pauli.PauliZ], [qubits[0], qubits[1]])
    my_qbob.add_local("result", measure, True)

    qsharp_code = my_qbob.formatted()
    print(qsharp_code)
    assert measure_array_items == qsharp_code
