import pytest
import os

@pytest.fixture()
def test_folder():
    return os.path.split(os.path.abspath(__file__))[0]


@pytest.fixture()
def hello_world():
    return """operation HelloWorld () : Unit {
    Message("Hello World!");
}"""


@pytest.fixture()
def hello_world_wrong():
    return """operation HelloWorld () : Foo {
    Bar("baz!");
}"""


@pytest.fixture()
def hello_world_qubit():
    return """operation HelloWorlds (register : Qubit[]) : Unit {
    H(register[0]);
    H(register[1]);
}"""


@pytest.fixture()
def measure_entangled_state():
    return """operation MeasureEntangledState () : Result[] {
    using (qubits = Qubit[2]) {
        H(qubits[0]);
        CNOT(qubits[0], qubits[1]);
        return [M(qubits[0]), M(qubits[1])];
    }
}"""


@pytest.fixture()
def measure_until_one():
    return """operation MeasureUntilOne () : Unit {
    using (q = Qubit()) {
        mutable result = Zero;
        repeat {
            H(q);
            set result = M(q);
        }
        until (result == One)
        fixup {
            Reset(q);
        }
    }
}"""


@pytest.fixture()
def prepare_entangled_state():
    return """operation PrepareEntangledState (qubits : Qubit[]) : Unit is Adj {
    H(qubits[0]);
    CNOT(qubits[0], qubits[1]);
}"""


@pytest.fixture()
def measure_entangled_state_using_prepare():
    return """operation MeasureEntangledState () : Result[] {
    using (qubits = Qubit[2]) {
        PrepareEntangledState(qubits);
        return [M(qubits[0]), M(qubits[1])];
    }
}"""


@pytest.fixture()
def h_x_h():
    return """operation HXH () : Unit {
    using (q = Qubit()) {
        within {
            H(q);
        } apply {
            X(q);
        }
    }
}"""


@pytest.fixture()
def is_plus():
    return """operation IsPlus (q : Qubit) : Bool {
    return Measure([PauliX], [q]) == Zero;
}"""


@pytest.fixture()
def is_minus():
    return """operation IsMinus (q : Qubit) : Bool {
    return Measure([PauliX], [q]) == One;
}"""


@pytest.fixture()
def teleport():
    return """operation Teleport (msg : Qubit, target : Qubit) : Unit {
    using (auxiliary = Qubit()) {
        H(auxiliary);
        CNOT(auxiliary, target);
        CNOT(msg, auxiliary);
        H(msg);

        if (Measure([PauliZ], [msg]) == One) {
            Z(target);
        }

        if (Measure([PauliZ], [auxiliary]) == One) {
            X(target);
        }
    }
}"""


@pytest.fixture()
def allocate_qubit():
    return """operation AllocateQubit () : Unit {
    using (q = Qubit()) {
        Z(q);
    }
}"""


@pytest.fixture()
def allocate_two_qubits():
    return """operation AllocateTwoQubits () : Unit {
    using (q = Qubit[2]) {
        Z(q[0]);
        Z(q[1]);
    }
}"""


@pytest.fixture()
def with_entrypoint():
    return """@EntryPoint()
operation RunProgram (nQubits : Int) : Unit {
    using (register = Qubit[nQubits]) {
        H(register[0]);
    }
}"""


@pytest.fixture()
def with_namespace_and_entrypoint():
    return """namespace Microsoft.Quantum.Foo {
    @EntryPoint()
    operation RunProgram (nQubits : Int) : Unit {
        using (register = Qubit[nQubits]) {
            H(register[0]);
        }
    }
}"""


@pytest.fixture()
def noop():
    return """operation DoNothing () : Unit {}"""


@pytest.fixture()
def noop_adj():
    return """operation DoNothingAdjoint () : Unit is Adj {}"""


@pytest.fixture()
def noop_ctl():
    return """operation DoNothingControl () : Unit is Ctl {}"""


@pytest.fixture()
def noop_adj_ctl():
    return """operation DoNothingAdjointControl () : Unit is Adj + Ctl {}"""


@pytest.fixture()
def noop_input():
    return """operation DoNothingWithInput (q : Qubit[]) : Unit {}"""


@pytest.fixture()
def noop_two_input():
    return """operation DoNothingWithMultipleInput (q : Qubit[], i : Int) : Unit {}"""


@pytest.fixture()
def single_gate():
    return """operation SingleGate (q : Qubit[]) : Unit {
    H(q[0]);
}"""


@pytest.fixture()
def two_gates():
    return """operation TwoGates (q : Qubit[]) : Unit {
    H(q[0]);
    CNOT(q[0], q[1]);
}"""


@pytest.fixture()
def measure_array():
    return """operation MeasureArray (qubits : Qubit[]) : Unit {
    let result = Measure([PauliZ, PauliZ], qubits);
}"""


@pytest.fixture()
def measure_array_items():
    return """operation MeasureArrayItems (qubits : Qubit[]) : Unit {
    let result = Measure([PauliZ, PauliZ], [qubits[0], qubits[1]]);
}"""


@pytest.fixture()
def namespace_with_import():
    return """namespace Foo {
    open Bar;
    open Baz;

    operation Spam () : Unit {}
}"""


@pytest.fixture()
def namespace_with_import_and_entrypoint():
    return """namespace Foo {
    open Test;

    @EntryPoint()
    operation Bar () : Unit {}
}"""


@pytest.fixture()
def controlled_x():
    return """operation ControlledX (qs : Qubit[]) : Unit {
    Controlled X([qs[0]], qs[1]);
}"""


@pytest.fixture()
def controlled_y():
    return """operation ControlledY (qs : Qubit[]) : Unit {
    Controlled Y([qs[0]], qs[1]);
}"""


@pytest.fixture()
def controlled_z():
    return """operation ControlledZ (qs : Qubit[]) : Unit is Adj + Ctl {
    Controlled Z([qs[0]], qs[1]);
}"""


@pytest.fixture()
def controlled_swap():
    return """operation ControlledSwap (control : Qubit, targets : Qubit[]) : Unit {
    Controlled SWAP([control], (targets[0],targets[1]));
}"""

@pytest.fixture()
def controlled_cnot():
    return """operation ControlledCNOT (qs : Qubit[]) : Unit {
    CCNOT(qs[0], qs[1], qs[2]);
}"""


@pytest.fixture()
def multiple_control():
    return """operation MultipleControl (qs : Qubit[]) : Unit {
    Controlled Y([qs[0], qs[1]], qs[2]);
}"""


@pytest.fixture()
def controlled_on_bit_string():
    return """operation TestControlledOnBitString (bits : Bool[], qs : Qubit[], target : Qubit) : Unit {
    ApplyControlledOnBitString(bits, H, qs, target);
    ApplyControlledOnBitString([true], H, [qs[0]], target);
    ApplyControlledOnBitString([true, false], H, [qs[0], qs[1]], target);
}"""


@pytest.fixture()
def operation_with_comments():
    return """namespace Foo {
    open Test;

    @EntryPoint()
    operation Bar () : Unit {
        // This is a comment
        Message("Bar");
        // Lorem ipsum
        // Dolor sit amet
    }
}"""
