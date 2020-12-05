#!/usr/bin/env python

"""Tests for `qbob` package."""
import qsharp
import pytest
from unittest.mock import Mock

from qbob import qbob


@pytest.fixture(params=["hello_world", "hello_world_qubit", "measure_until_one", "h_x_h", "teleport",
 "prepare_entangled_state", "allocate_qubit", "allocate_two_qubits", "noop", "noop_adj", "noop_ctl",
 "noop_adj_ctl"])

def operation_unit(request):
    return request.getfixturevalue(request.param)


@pytest.fixture(params=["measure_entangled_state", "measure_entangled_state_using_prepare"])
def operation_measure(request, prepare_entangled_state):
    if request.param == "measure_entangled_state_using_prepare":
        qsharp.compile(prepare_entangled_state)
    return request.getfixturevalue(request.param)


def test_compile_units(operation_unit):
    program = qsharp.compile(operation_unit)
    program.simulate()


def test_compile_wrong(hello_world_wrong):
    with pytest.raises(TypeError):
        program = qsharp.compile(hello_world_wrong)


def test_compile_measure(operation_measure):
    program = qsharp.compile(operation_measure)
    result = program.simulate()


def test_hello_worlds(hello_world_qubit):
    qsharp.compile(hello_world_qubit)
    entrypoint = qsharp.compile("""operation Program () : Unit {
    using (qubit = Qubit[2]) {
        HelloWorlds(qubit);
    }
}""")
    entrypoint.simulate()


def test_is_plus(is_plus):
    qsharp.compile(is_plus)
    entrypoint = qsharp.compile("""operation Program () : Bool {
    using (qubit = Qubit()) {
        Reset(qubit);
        H(qubit);
        return IsPlus(qubit);
    }
}""")
    assert entrypoint.simulate()


def test_is_minus(is_minus):
    qsharp.compile(is_minus)
    entrypoint = qsharp.compile("""operation Program () : Bool {
    using (qubit = Qubit()) {
        Reset(qubit);
        X(qubit);
        H(qubit);
        return IsMinus(qubit);
    }
}""")
    assert entrypoint.simulate()


def test_teleport(is_minus, teleport):
    qsharp.compile(is_minus)
    qsharp.compile(teleport)
    entrypoint = qsharp.compile("""operation Program (message : Bool) : Bool {
    using ((msg, target) = (Qubit(), Qubit())) {
        Reset(msg);
        Reset(target);
        if (message == true) {
            X(msg);
        }
        H(msg);
        Teleport(msg, target);
        return IsMinus(target);
    }
}""")
    assert entrypoint.simulate(message=True)
    assert not entrypoint.simulate(message=False)


def test_noop_input(noop_input):
    qsharp.compile(noop_input)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using (qubit = Qubit[1] {
            DoNothingWithInput(qubit);
        }
    }""")
    entrypoint.simulate()


def test_noop_input(noop_two_input):
    qsharp.compile(noop_two_input)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using (qubits = Qubit[2]) {
            DoNothingWithMultipleInput(qubits, 2);
        }
    }""")
    entrypoint.simulate()


def test_single_gate(single_gate):
    qsharp.compile(single_gate)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using (qubits = Qubit[1]) {
            SingleGate(qubits);
        }
    }""")
    entrypoint.simulate()


def test_two_gates(two_gates):
    qsharp.compile(two_gates)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using (qubits = Qubit[2]) {
            TwoGates(qubits);
        }
    }""")
    entrypoint.simulate()


def test_measure_array(measure_array):
    qsharp.compile(measure_array)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qubits = Qubit[2]) {
            MeasureArray(qubits);
    }
}""")
    entrypoint.simulate()


def test_measure_array_items(measure_array_items):
    qsharp.compile(measure_array_items)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qubits = Qubit[2]) {
            MeasureArrayItems(qubits);
    }
}""")
    entrypoint.simulate()

def test_controlled_z(controlled_z):
    qsharp.compile(controlled_z)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qubits = Qubit[2]) {
            ControlledZ(qubits);
    }
}""")
    entrypoint.simulate()

def test_controlled_x(controlled_x):
    qsharp.compile(controlled_x)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qubits = Qubit[2]) {
            ControlledX(qubits);
    }
}""")
    entrypoint.simulate()

def test_controlled_z(controlled_y):
    qsharp.compile(controlled_y)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qubits = Qubit[2]) {
            ControlledY(qubits);
    }
}""")
    entrypoint.simulate()

def test_controlled_cnot(controlled_cnot):
    qsharp.compile(controlled_cnot)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qubits = Qubit[3]) {
            ControlledCNOT(qubits);
    }
}""")
    entrypoint.simulate()

def test_controlled_swap(controlled_swap):
    qsharp.compile(controlled_swap)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qubits = Qubit[3]) {
            ControlledSwap(qubits[0], [qubits[1], qubits[2]]);
    }
}""")
    entrypoint.simulate()



def test_multiple_control(multiple_control):
    qsharp.compile(multiple_control)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qubits = Qubit[3]) {
            MultipleControl(qubits);
    }
}""")
    entrypoint.simulate()

def test_controlled_on_bit_string(controlled_on_bit_string):
    qsharp.compile(controlled_on_bit_string)
    entrypoint = qsharp.compile("""operation Program () : Unit {
        using(qs = Qubit[3]) {
            TestControlledOnBitString([false, true], [qs[0], qs[1]], qs[3]);
    }
}""")
    entrypoint.simulate()
