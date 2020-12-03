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


# Some classes for debugging
from qbob.formatter import QSharpListener, QSharpFormatter

class QSharpDebugListener(QSharpListener):
    """Listener for QSharp Parse tree that formats Q# code
    """
    def __init__(self, *args, **kwargs):
        super().__init__(debug=True, *args, **kwargs)


class QSharpDebugFormatter(QSharpFormatter):
    listener_cls = QSharpDebugListener


def test_formatter(unformatted, formatted):
    formatter = QSharpFormatter()
    assert formatter.format_input(unformatted) == formatted


def test_format_file(test_file, formatted):
    formatter = QSharpFormatter()
    assert formatter.format_file(test_file) == formatted


@pytest.mark.parametrize("fixture_name", 
    [
        "hello_world", 
        "hello_world_wrong", 
        "hello_world_qubit", 
        "measure_until_one",
        "h_x_h",
        #"teleport"
    ]
)#, "measure_until_one", "h_x_h", "teleport"])
def test_format_operations_unit(fixture_name, request):
    data = request.getfixturevalue(fixture_name)
    formatter = QSharpFormatter()
    assert formatter.format_input(data) == data


def test_case(hello_world, measure_until_one):
    # formatter = QSharpDebugFormatter()
    # print(formatter.format_input(hello_world))
    # print("\n")

    data = measure_until_one

    formatter = QSharpDebugFormatter()
    print(formatter.format_input(data))
    print("\n")

    formatter = QSharpFormatter()
    print(formatter.format_input(data))
    print(data)
    print("\n")

    assert formatter.format_input(data) == data
