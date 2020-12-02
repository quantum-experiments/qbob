import pytest
import os
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from qbob.formatter import QSharpFormatter

@pytest.fixture()
def test_file(test_folder):
    return os.path.join(test_folder, "test_formatter.qs")


@pytest.fixture()
def unformatted():
    return """namespace            Microsoft.Quantum.Foo {  
         operation Test () : String {
        
          let test = "Hello world!";
   return test;}
    
}"""


@pytest.fixture()
def formatted():
    return """namespace Microsoft.Quantum.Foo {
    operation Test () : String {
        let test = "Hello world!";
        return test;
    }
}"""


def test_formatter(unformatted, formatted):
    formatter = QSharpFormatter()
    assert formatter.format_input(unformatted) == formatted


def test_format_file(test_file, formatted):
    formatter = QSharpFormatter()
    assert formatter.format_file(test_file) == formatted


def test_hello_world(hello_world):
    formatter = QSharpFormatter()
    assert formatter.format_input(hello_world) == hello_world
