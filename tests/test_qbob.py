#!/usr/bin/env python

"""Tests for `qbob` package.""" 

import pytest
from typing import List

import qsharp
from qbob import qbob
from qbob.intrinsics import *
from qbob.types import *
from qbob.utils import Equals


def without_whitespace(string):
    return "".join(string.split())


def no_whitespace_equals(expected : str, actual : str):
    return without_whitespace(actual) == without_whitespace(expected)


def test_empty_operation(noop):
    my_qbob = qbob.OperationBuilder("DoNothing")

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(noop, qsharp_code)


def test_adjoint_operation(noop_adj):
    my_qbob = qbob.OperationBuilder("DoNothingAdjoint")
    my_qbob.is_adj = True

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(noop_adj, qsharp_code)


def test_control_operation(noop_ctl):
    my_qbob = qbob.OperationBuilder("DoNothingControl")
    my_qbob.is_ctl = True

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(noop_ctl, qsharp_code)


def test_adjoint_and_control_operation(noop_adj_ctl):
    my_qbob = qbob.OperationBuilder("DoNothingAdjointControl")
    my_qbob.is_adj = True
    my_qbob.is_ctl = True

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(noop_adj_ctl, qsharp_code)


def test_empty_operation_with_input(noop_input):
    my_qbob = qbob.OperationBuilder("DoNothingWithInput")
    my_qbob.input("q", List[Qubit])
    
    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(noop_input, qsharp_code)


def test_empty_operation_with_multiple_input(noop_two_input):
    my_qbob = qbob.OperationBuilder("DoNothingWithMultipleInput")
    my_qbob.input("q", List[Qubit])
    my_qbob.input("i", int)
    
    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(noop_two_input, qsharp_code)


def test_single_gate(single_gate):
    my_qbob = qbob.OperationBuilder("SingleGate")
    qubits = my_qbob.input("q", List[Qubit])
    
    my_qbob += H(qubits[0])
    
    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(single_gate, qsharp_code)


def test_two_gates(two_gates):
    my_qbob = qbob.OperationBuilder("TwoGates")
    qubits = my_qbob.input("q", List[Qubit])
    
    my_qbob += H(qubits[0])
    my_qbob += CNOT(qubits[0], qubits[1])
    
    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(two_gates, qsharp_code)


def test_allocate_qubit(allocate_qubit):
    my_qbob = qbob.OperationBuilder("AllocateQubit")
    with my_qbob.allocate_qubits("q", 1) as q:
        my_qbob += Z(q)

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(allocate_qubit, qsharp_code)


def test_allocate_two_qubits(allocate_two_qubits):
    my_qbob = qbob.OperationBuilder("AllocateTwoQubits")
    with my_qbob.allocate_qubits("q", 2) as q:
        my_qbob += Z(q[0])
        my_qbob += Z(q[1])

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(allocate_two_qubits, qsharp_code)


def test_measure_entangled_state(measure_entangled_state):
    my_qbob = qbob.OperationBuilder("MeasureEntangledState")
    with my_qbob.allocate_qubits("qubits", 2) as q:
        my_qbob += H(q[0])
        my_qbob += CNOT(q[0], q[1])
        my_qbob.returns([M(q[0]), M(q[1])])

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(measure_entangled_state, qsharp_code)


def test_within_apply(h_x_h):
    my_qbob = qbob.OperationBuilder("HXH")
    with my_qbob.allocate_qubits("q", 1) as q:
        with my_qbob.within(H(q)):
            my_qbob += X(q)

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(h_x_h, qsharp_code)


def test_measure_until_one(measure_until_one):
    my_qbob = qbob.OperationBuilder("MeasureUntilOne")
    with my_qbob.allocate_qubits("q", 1) as q:
        result = my_qbob.add_local("result", Zero)
        with my_qbob.repeat_until(result == One,
                fixup = Reset(q)):
            my_qbob += H(q)
            my_qbob.set_local(result, M(q))

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(measure_until_one, qsharp_code)


def test_hello_world(hello_world):
    my_qbob = qbob.OperationBuilder("HelloWorld")
    my_qbob += print("Hello World!")

    qsharp_code = my_qbob.to_str()
    assert no_whitespace_equals(hello_world, qsharp_code)


def test_hello_world_qubit(hello_world_qubit):
    my_qbob = qbob.OperationBuilder("HelloWorlds")
    qubits = my_qbob.input("register", List[Qubit])

    my_qbob += H(qubits[0])
    my_qbob += H(qubits[1])

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(hello_world_qubit, qsharp_code)


def test_nested_operations(prepare_entangled_state, measure_entangled_state_using_prepare):
    prepare_qbob = qbob.OperationBuilder("PrepareEntangledState")
    prepare_qbob.is_adj = True
    qubits = prepare_qbob.input("qubits", List[Qubit])
    prepare_qbob += H(qubits[0])
    prepare_qbob += CNOT(qubits[0], qubits[1])

    qsharp_code = prepare_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace(prepare_entangled_state)
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()

    measure_qbob = qbob.OperationBuilder("MeasureEntangledState")
    with measure_qbob.allocate_qubits("qubits", 2) as q:
        measure_qbob += prepare_qbob(q)
        measure_qbob.returns([M(q[0]), M(q[1])])

    qsharp_code = measure_qbob.to_str()
    print(qsharp_code)
    assert (without_whitespace(measure_entangled_state_using_prepare)
            == without_whitespace(qsharp_code))

    compiled_op = qsharp.compile(qsharp_code)
    compiled_op()


def test_prepare_entangled_state(prepare_entangled_state):
    my_qbob = qbob.OperationBuilder("PrepareEntangledState")
    my_qbob.is_adj = True
    qubits = my_qbob.input("qubits", List[Qubit])

    my_qbob += H(qubits[0])
    my_qbob += CNOT(qubits[0], qubits[1])

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(prepare_entangled_state, qsharp_code)


def test_is_plus(is_plus):
    my_qbob = qbob.OperationBuilder("IsPlus")
    q = my_qbob.input("q", Qubit)
    my_qbob.returns(Equals(Measure([Pauli.PauliX], [q]), Zero))

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(is_plus, qsharp_code)


def test_is_minus(is_minus):
    my_qbob = qbob.OperationBuilder("IsMinus")
    q = my_qbob.input("q", Qubit)
    my_qbob.returns(Equals(Measure([Pauli.PauliX], [q]), One))

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(is_minus, qsharp_code)


def test_teleport(teleport):
    my_qbob = qbob.OperationBuilder("Teleport")
    msg = my_qbob.input("msg", Qubit)
    target = my_qbob.input("target", Qubit)
    with my_qbob.allocate_qubits("auxiliary", 1) as aux:
        my_qbob += H(aux)
        my_qbob += CNOT(aux, target)
        my_qbob += CNOT(msg, aux)
        my_qbob += H(msg)
        with my_qbob.if_statement(Equals(Measure([Pauli.PauliZ], [msg]), One)):
            my_qbob += Z(target)
        with my_qbob.if_statement(Equals(Measure([Pauli.PauliZ], [aux]), One)):
            my_qbob += X(target)

    qsharp_code = my_qbob.to_str()
    print(qsharp_code)
    assert no_whitespace_equals(teleport, qsharp_code)

#TODO: test_measure_entangled_state_using_prepare -- add after BOB 3 (nested operations)
