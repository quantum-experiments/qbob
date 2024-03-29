# QBOB |👷‍♀️> (Q# Basic Operation Builder)

QBOB (Q# Basic Operation Builder) is a Python tool for generating Q# code, which it returns in string format to directly compile using `qsharp`. The package also includes QPAM (Q# Project Architect Manager) which can use one or more QBOBs to output the generated Q# code to a file to run as a Q# project on the command line.

## QBOB |👷🏾‍♂️> example usage

```python
from qbob import qbob, qpam
from qbob.intrinsics import Message, H, M

my_qbob = qbob.OperationBuilder("HelloWorld", entrypoint=True)
my_qbob += Message("Hello World!")
with my_qbob.allocate_qubit("q") as q:
    my_qbob += H(q)
    my_qbob.returns(M(q))

print(my_qbob.build())
```

generates

```qsharp
@EntryPoint()
operation HelloWorld () : Result {
    Message("Hello World!");
    using (q = Qubit()) {
        H(q);
        return M(q);
    }
}
```

To run using `qsharp`:

```python
hello_world = my_qbob.compile()
hello_world()
```

outputs

```bash
Hello World!
0
```

### Debugging

We can also use the debugging feature to print the intermediate qubit state as a comment into the generated Q# code using `debug=True`.

```python
my_qbob = qbob.OperationBuilder("HelloWorld", entrypoint=True, debug=True)
with my_qbob.allocate_qubit("q") as q:
    my_qbob += H(q)
    my_qbob.log_state(q)
    my_qbob.returns(M(q))

print(my_qbob.build())
```

generates

```qsharp
@EntryPoint()
operation HelloWorld () : Result {
    using (q = Qubit()) {
        H(q);
        // # wave function for qubits with ids (least to most significant): 0
        // ∣0❭:	 0.707107 +  0.000000 i	 == 	***********          [ 0.500000 ]     --- [  0.00000 rad ]
        // ∣1❭:	 0.707107 +  0.000000 i	 == 	***********          [ 0.500000 ]     --- [  0.00000 rad ]
        return M(q);
    }
}
```

## QPAM |👷🏻‍♀️> example usage

QPAM, the Q# Project Architect Manager, uses one or more QBOBs to generate a .qs file and .csproj project file that can be compiled and run from the terminal. It also adds a namespace scope and opens any namespace dependencies.

```python
my_qpam = qpam.ProgramArchitect("MyProject")
my_qpam.add_operations(my_qbob)
my_qpam.create_project(".")
```

where

```bash
$ cat Program.qs
namespace MyProject {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    @EntryPoint()
    operation HelloWorld () : Result {
        using (q = Qubit()) {
            H(q);
            // # wave function for qubits with ids (least to most significant): 0
            // ∣0❭:	 0.707107 +  0.000000 i	 == 	***********          [ 0.500000 ]     --- [  0.00000 rad ]
            // ∣1❭:	 0.707107 +  0.000000 i	 == 	***********          [ 0.500000 ]     --- [  0.00000 rad ]
            return M(q);
        }
    }
}
```

To run the program from the command line:

```bash
$ dotnet run
Hello World!
```

For more examples, see the [example notebook](examples/qbob_101.ipynb).
