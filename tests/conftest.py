import pytest

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
    return """operation MeasureEntangledState() : Result[] {
    using (qubits = Qubit[2]) {
        H(qubits[0]);
        CNOT(qubits[0], qubits[1]);
        return [M(qubits[0]), M(qubits[1])];
    }
}"""


@pytest.fixture()
def measure_until_one():
    return """operation MeasureUntilOne() : Unit {
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
    return """operation PrepareEntangledState(qubits : Qubit[]) : Unit is Adj {
    H(qubits[0]);
    CNOT(qubits[0], qubits[1]);
}"""


@pytest.fixture()
def measure_entangled_state_using_prepare(prepare_entangled_state):
    import qsharp
    qsharp.compile(prepare_entangled_state)
    return """operation MeasureEntangledState() : Result[] {
    using (qubits = Qubit[2]) {
        PrepareEntangledState(qubits);
        return [M(qubits[0]), M(qubits[1])];
    }
}"""


@pytest.fixture()
def h_x_h():
    return """operation HXH() : Unit {
    using (q = Qubit()) {
        within {
            H(q);
        } apply {
            X(q);
        }
    }
}"""


@pytest.fixture()
def is_zero():
    return """operation IsZero(q: Qubit) : Bool {
    return (Measure([PauliX], [q]) == Zero);
}"""


@pytest.fixture()
def is_one():
    return """operation IsOne(q: Qubit) : Bool {
    return (Measure([PauliX], [q]) == One);
}"""


@pytest.fixture()
def teleport():
    return """operation Teleport (msg : Qubit, target : Qubit) : Unit {
    using (auxiliary = Qubit()) {
        H(auxiliary);
        CNOT(auxiliary, target);
        CNOT(msg, auxiliary);
        H(msg);

        if (Measure([PauliX], [msg]) == One) {
            Z(target);
        }

        if (Measure([PauliX], [auxiliary]) == One) {
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
