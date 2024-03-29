#!/usr/bin/env python

"""Tests for `qpam` module.""" 

import pytest
import os
import qsharp

from qbob import qbob, qpam
from qbob.intrinsics import *
from qbob.types import *


def test_empty_project(tmp_path):
    '''Tests creating a .csproj file only.'''
    my_qpam = qpam.ProgramArchitect("EmptyProject")
    project_path = my_qpam.create_project(tmp_path)

    assert os.path.exists(project_path)
    qsharp.projects.add(str(project_path))
    qsharp.reload()

def test_file(tmp_path):
    '''Tests creating .csproj and .qs files individually.'''
    my_qpam = qpam.ProgramArchitect("TestProject")
    project_path = my_qpam.save_csproj_file(tmp_path, "HelloWorld.csproj")

    my_qbob = qbob.OperationBuilder("HelloWorld")
    my_qbob += Message("Hello World!")
    my_qpam.add_operations(my_qbob)
    file_path = my_qpam.save_qs_file(tmp_path, "HelloWorld.qs")

    assert os.path.exists(project_path)
    assert os.path.exists(file_path)
    qsharp.projects.add(str(project_path))
    qsharp.reload()
    assert "TestProject.HelloWorld" in qsharp.get_available_operations()


def test_file_with_comments(tmp_path):
    '''Tests creating .csproj and .qs files individually.'''
    my_qpam = qpam.ProgramArchitect("TestProject")
    project_path = my_qpam.save_csproj_file(tmp_path, "HelloWorld.csproj")

    my_qbob = qbob.OperationBuilder("HelloWorld", debug=True)
    my_qbob += Message("Hello World!")
    with my_qbob.allocate_qubit("q") as q:
        my_qbob += H(q)
        my_qbob.log_state(q)
        my_qbob += Reset(q)
    my_qpam.add_operations(my_qbob)
    file_path = my_qpam.save_qs_file(tmp_path, "HelloWorld.qs")

    with open(file_path, encoding="utf8") as f:
        file_contents = f.read()

    assert file_contents == """namespace TestProject {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation HelloWorld () : Unit {
        Message("Hello World!");
        using (q = Qubit()) {
            H(q);
            // # wave function for qubits with ids (least to most significant): 0
            // ∣0❭:	 0.707107 +  0.000000 i	 == 	***********          [ 0.500000 ]     --- [  0.00000 rad ]
            // ∣1❭:	 0.707107 +  0.000000 i	 == 	***********          [ 0.500000 ]     --- [  0.00000 rad ]
            Reset(q);
        }
    }
}"""


def test_executable(tmp_path):
    '''Tests creating a Q# executable project with source code.'''
    my_qbob = qbob.OperationBuilder("HelloWorld")
    my_qbob.is_entrypoint = True
    my_qbob += Message("Hello World!")

    my_qpam = qpam.ProgramArchitect("HelloWorldExecutable")
    my_qpam.is_executable = True
    my_qpam.add_operations(my_qbob)
    project_path = my_qpam.create_project(tmp_path)

    assert os.path.exists(project_path)
    qsharp.projects.add(str(project_path))
    qsharp.reload()
    assert "HelloWorldExecutable.HelloWorld" in qsharp.get_available_operations()


def test_hello_world(tmp_path):
    '''Tests creating a Q# library project with source code.'''
    qbob1 = qbob.OperationBuilder("HelloWorld")
    qbob1 += Message("Hello World!")

    qbob2 = qbob.OperationBuilder("HelloWorlds")
    qubits = qbob2.input("register", List[Qubit])
    qbob2 += H(qubits[0])
    qbob2 += H(qubits[1])
    qbob2 += qbob1()

    my_qpam = qpam.ProgramArchitect("HelloWorldLibrary")
    my_qpam.add_operations(qbob1, qbob2)
    project_path = my_qpam.create_project(tmp_path)

    assert os.path.exists(project_path)
    qsharp.projects.add(str(project_path))
    qsharp.reload()
    assert "HelloWorldLibrary.HelloWorld" in qsharp.get_available_operations()
    assert "HelloWorldLibrary.HelloWorlds" in qsharp.get_available_operations()
