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
    return """open Microsoft.Quantum.Intrinsic;
operation MeasureEntangledState() : Result[] {
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
def measure_entangled_state_using_prepare():
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
def is_plus():
    return """operation IsPlus(q: Qubit) : Bool {
    return (Measure([PauliX], [q]) == Zero);
}"""


@pytest.fixture()
def is_minus():
    return """operation IsMinus(q: Qubit) : Bool {
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

        if (Measure([PauliZ], [msg]) == One) {
            Z(target);
        }

        if (Measure([PauliZ], [auxiliary]) == One) {
            X(target);
        }
    }
}"""
