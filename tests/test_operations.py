#!/usr/bin/env python

"""Tests for `qbob` package."""
import qsharp
import pytest
from unittest.mock import Mock

from qbob import qbob


@pytest.fixture(params=["hello_world", "hello_world_qubit", "measure_until_one", "h_x_h", "teleport"])
def operation_unit(request):
    return request.getfixturevalue(request.param)


@pytest.fixture(params=["measure_entangled_state", "measure_entangled_state_using_prepare"])
def operation_measure(request):
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
