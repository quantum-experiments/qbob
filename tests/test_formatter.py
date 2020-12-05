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
    print(formatter.format_input(unformatted))
    print("\n")
    print(formatted)
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
        "teleport",
        "measure_entangled_state", 
        "measure_entangled_state_using_prepare",
        "prepare_entangled_state",
        "is_plus",
        "is_minus",
        "allocate_qubit",
        "allocate_two_qubits",
        "with_entrypoint",
        "with_namespace_and_entrypoint",
        "noop",
        "noop_adj",
        "noop_ctl",
        "noop_adj_ctl",
        "noop_input",
        "noop_two_input",
        "single_gate",
        "two_gates",
        "namespace_with_import",
        "namespace_with_import_and_entrypoint",
<<<<<<< HEAD
        "controlled_x",
        "controlled_y",
        "controlled_z",
        "controlled_swap",
        "controlled_cnot",
        "multiple_control",
        "controlled_on_bit_string"
=======
        "controlled_gate",
        "operation_with_comments"
>>>>>>> 2cffb699a3c4cf5f4b2925c6a8867194987168fc
    ]
)
def test_format_operations_unit(fixture_name, request):
    data = request.getfixturevalue(fixture_name)
    formatter = QSharpFormatter()
    assert formatter.format_input(data) == data
