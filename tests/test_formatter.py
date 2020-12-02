import pytest
import os
from antlr4 import *

from qbob.formatter import QSharpLexer, QSharpListener, QSharpParser

@pytest.fixture()
def test_file(test_folder):
    return os.path.join(test_folder, "test_formatter.qs")

@pytest.fixture()
def formatted():
    return """namespace Microsoft.Quantum.Foo {
    operation Test () : String {
        let test = "Hello world!";
        return test;
    }
}"""


def test_formatter(test_file, formatted):
    input_stream = FileStream(test_file)
    lexer = QSharpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = QSharpParser(stream)
    tree = parser.namespace()
    printer = QSharpListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    assert printer.value == formatted
