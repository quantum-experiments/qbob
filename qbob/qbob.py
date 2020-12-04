"""Define the OperationBuilder class."""
import tempfile
import uuid
import os

from contextlib import contextmanager
from typing import List, Union, _GenericAlias

from qbob.token import Token
from qbob.types import to_qsharp_type, to_qsharp_value, to_qsharp_escaped_string
from qbob.formatter import QSharpFormatter


NEWLINE = "\n"
TEMP_DIR_KEYWORD = "qbob_state_log_temp_dir"


class OperationBuilder:

    _OPERATION_TEMPLATE = \
        """{attributes} operation {name} ( {arguments} ) : {return_type} {characteristics}
        {{
            {statements}
        }}"""

    def __init__(self, operation_name: str, entrypoint: bool=False, adj: bool = False, ctl: bool = False, 
        debug: bool = False):
        self.operation_name = operation_name
        self.input_parameters = {}
        self.is_adj = adj
        self.is_ctl = ctl
        self.is_entrypoint = entrypoint
        self._state_log = {}
        self.statements = []
        self.return_type = "Unit"
        self.debug = debug

    @property
    def attributes(self) -> str:
        return "@EntryPoint()" if self.is_entrypoint else ""

    @property
    def arguments(self) -> str:
        return ",".join(
            [
                f"{n} : {to_qsharp_type(t)}" for n, t in self.input_parameters.items()
            ]
        )

    @property
    def characteristics(self) -> str:
        chars = ("is Adj + Ctl" if self.is_adj and self.is_ctl
                else "is Adj" if self.is_adj
                else "is Ctl" if self.is_ctl
                else "")
        return chars

    def op_statements(self, with_state_log: bool = False) -> str:
        if not with_state_log:
            # Only return statements that don't include state logging
            statements = [st for st in self.statements if st not in [f"{s};" for s in self._state_log.values()]]
            return NEWLINE.join(statements)
        return NEWLINE.join(self.statements)

    def to_str(self, with_state_log: bool = False) -> str:
        return self._OPERATION_TEMPLATE.format(
            name=self.operation_name,
            attributes=self.attributes,
            arguments=self.arguments,
            return_type=self.return_type,
            characteristics=self.characteristics,
            statements=self.op_statements(with_state_log=with_state_log)
        )

    def formatted(self, with_state_log: bool = False):
        formatter = QSharpFormatter()
        unformatted_code = self.to_str(with_state_log=with_state_log)
        return formatter.format_input(unformatted_code)

    def formatted_debug(self) -> str:
        """Format the Q# code and insert the output of DumpRegister 
        (which was added using qbob.state_log) into the code

        # Debug steps:
        # 0. generate Q# code ("source" file)
        # 1. replace the temp folder placeholder in the Q# "debug" code with an actual temp folder
        # 2. compile and run, output to temp files
        # 3. read files and insert back into "source" file as comments
        # 4. return new Q# code with comments as string:

        # Hi from QBOB!
        # Falling back to base DumpRegister.
        # Falling back to base DumpRegister.
        # Falling back to base DumpRegister.
        # operation TestDumpMachine () : Result[] {
        #     Message("Hi from QBOB!");
        #     using (q = Qubit[3]) {
        #         H(q[0]);
        #         // # wave function for qubits with ids (least to most significant): 0
        #         // ∣0❭:	 0.707107 +  0.000000 i	 == 	***********          [ 0.500000 ]     --- [  0.00000 rad ]
        #         // ∣1❭:	 0.707107 +  0.000000 i	 == 	***********          [ 0.500000 ]     --- [  0.00000 rad ]
        #         H(q[1]);
        #         // # wave function for qubits with ids (least to most significant): 1
        #         // ∣0❭:	 0.707107 +  0.000000 i	 == 	**********           [ 0.500000 ]     --- [  0.00000 rad ]
        #         // ∣1❭:	 0.707107 +  0.000000 i	 == 	**********           [ 0.500000 ]     --- [  0.00000 rad ]
        #         X(q[2]);
        #         // # wave function for qubits with ids (least to most significant): 2
        #         // ∣0❭:	 0.000000 +  0.000000 i	 == 	                     [ 0.000000 ]                   
        #         // ∣1❭:	 1.000000 +  0.000000 i	 == 	******************** [ 1.000000 ]     --- [  0.00000 rad ]
        #         return [M(q[0]), M(q[1]), M(q[2])];
        #     }
        # }

        :return: Formatted code including text representation of qubit state
        :rtype: str
        """
        code = self.formatted(with_state_log=True)
        with tempfile.TemporaryDirectory() as temp_dir:
            code_to_compile = code.replace(TEMP_DIR_KEYWORD, to_qsharp_escaped_string(temp_dir))

            # Compile the program with DumpRegister operations and save to files in temp dir
            import qsharp
            qsharp_callable = qsharp.compile(code_to_compile)
            qsharp_callable.simulate()
            
            # Read files and replace DumpRegister lines with file contents
            new_code = code
            for guid, token in self._state_log.items():
                with open(os.path.join(temp_dir, guid), encoding="utf8") as f:
                    state_log = f.read()

                # ugly hack...
                indentation = " " * new_code[:new_code.index(str(token))][::-1].index("\n")
                state_log_comment = "// " + state_log.rstrip("\n").replace("\n", f"\n{indentation}// ")
                new_code = new_code.replace(f"{token};", state_log_comment)
        
        return new_code


    def build(self) -> str:
        """Generate formatted Q# code from the builder

        :return: Formatted Q# code
        :rtype: str
        """
        if self.debug is True and self._state_log:
            return self.formatted_debug()
        return self.formatted()

    def compile(self):
        import qsharp
        return qsharp.compile(self.formatted())

    def generate_temporary_file(self):
        if self.temp_dir is None:
            with tempfile.TemporaryDirectory() as temp_dir:
                self.temp_dir = temp_dir

    def log_state(self, register: Union[Token, List[Token]]):
        if self.input_parameters:
            raise IOError("Cannot log state for non-deterministic operation with input parameters.")

        if self.debug is True:
            from qbob.diagnostics import DumpRegister
            guid = str(uuid.uuid4())
            temp_file_location = os.path.join(TEMP_DIR_KEYWORD, guid)
            token = DumpRegister(temp_file_location, register)
            self += token
            self._state_log[guid] = token # keep track of guid to dumpregister tokens

    def __call__(self, *args) -> Token:
        assert len(args) == len(self.input_parameters)
        args_as_str = [str(arg) for arg in args]
        return Token(f"{self.operation_name}({','.join(args_as_str)})", self.return_type)

    def input(self, parameter_name: str, parameter_type: Union[type, _GenericAlias]) -> Token:
        assert isinstance(parameter_name, str)
        assert (isinstance(parameter_type, type)
                or isinstance(parameter_type, _GenericAlias))
        self.input_parameters[parameter_name] = parameter_type

        return Token(parameter_name, to_qsharp_type(parameter_type))

    def add_local(self, name: str, value: object, immutable: bool = False) -> Token:
        self.statements.append(f"{'let' if immutable else 'mutable'} {name} = {to_qsharp_value(value)};")
        return Token(name, to_qsharp_type(type(value)))

    def set_local(self, local: Token, value: object) -> None:
        self.statements.append(f"set {local} = {value};")

    def returns(self, *return_tokens) -> None:
        def to_qsharp_return_value(return_token: Union[List, Token]) -> str:
            if isinstance(return_token, list):
                return "[" + ",".join([to_qsharp_return_value(token) for token in return_token]) + "]"
            return return_token.name
        
        def to_qsharp_return_type(return_token: Union[List, Token]) -> str:
            if isinstance(return_token, list):
                return f"{to_qsharp_return_type(return_token[0])}[]"
            return return_token.type

        ret_val = ','.join([to_qsharp_return_value(r) for r in return_tokens])
        self.statements.append(f"return {ret_val};")

        self.return_type = ','.join([to_qsharp_return_type(r) for r in return_tokens])

    @contextmanager
    def allocate_qubit(self, register_name: str):
        yield self.allocate_qubits(register_name=register_name, num_qubits=1)
    
    
    @contextmanager
    def allocate_qubits(self, register_name: str, num_qubits: Union[int, Token]):
        assert isinstance(num_qubits, Token) or num_qubits > 0

        if isinstance(num_qubits, int) and num_qubits == 1:
            self.statements.append(f"using ({register_name} = Qubit())")
            type_name = "Qubit"
        else:
            self.statements.append(f"using ({register_name} = Qubit[{num_qubits}])")
            type_name = "Qubit[]"
        
        self.statements.append("{")
        try:
            yield Token(register_name, type_name)
        finally:
            self.statements.append("}")

    @contextmanager
    def within(self, expressions: Union[Token, List[Token]]):
        if not isinstance(expressions, list):
            expressions = [expressions]
        
        self.statements.append("within {")
        for expression in expressions:
            self += expression
        self.statements.append("} apply {")
        try:
            yield
        finally:
            self.statements.append("}")
    
    @contextmanager
    def repeat_until(self, condition: Token, fixup: Union[Token, List[Token]] = []):
        assert condition.type == to_qsharp_type(bool)
        if not isinstance(fixup, list):
            fixup = [fixup]
        
        self.statements.append("repeat {")
        try:
            yield
        finally:
            self.statements.append("}")
            self.statements.append(f"until ({condition})")
            if fixup:
                self.statements.append("fixup {")
                for expression in fixup:
                    self += expression
                self.statements.append("}")

    @contextmanager
    def if_statement(self, condition: Token):
        assert condition.type == "Bool"
        self.statements.append(f"if ({condition}) {{")
        try:
            yield
        finally:
            self.statements.append("}")

    def __iadd__(self, expression: Token) -> 'OperationBuilder':
        self.statements.append(f"{expression};")
        return self
