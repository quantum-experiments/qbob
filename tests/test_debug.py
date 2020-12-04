from qbob import qbob
from qbob.intrinsics import Message, H, M, X
from qbob.diagnostics import DumpMachine, DumpRegister

def test_debug(tmp_path):
    def file_location(n):
        return tmp_path / f"test{n}.txt"
    
    my_qbob = qbob.OperationBuilder("TestDumpMachine")
    my_qbob += Message("Hi from QBOB!")
    
    with my_qbob.allocate_qubits("q", 1) as q:
        my_qbob += H(q)
        my_qbob += DumpRegister(file_location(1), [q])
        my_qbob += H(q)
        my_qbob += DumpRegister(file_location(2), [q])
        my_qbob += X(q)
        my_qbob += DumpRegister(file_location(3), [q])
        my_qbob.returns(M(q))

    code = my_qbob.build()
    print(code)
    test = my_qbob.compile()
    test()

    with open(file_location(1)) as f:
        print(f.read())

    with open(file_location(2)) as f:
        print(f.read())

    with open(file_location(3)) as f:
        print(f.read())


def test_debug_register(tmp_path):
    def file_location(n):
        return tmp_path / f"test{n}.txt"
    
    my_qbob = qbob.OperationBuilder("TestDumpMachine")
    my_qbob += Message("Hi from QBOB!")
    
    with my_qbob.allocate_qubits("q", 5) as q:
        my_qbob += H(q[0])
        my_qbob += DumpRegister(file_location(1), [q[0]])
        my_qbob += H(q[0])
        my_qbob += DumpRegister(file_location(2), [q[0]])
        my_qbob += X(q[1])
        my_qbob += DumpRegister(file_location(3), [q[1]])
        my_qbob.returns(M(q[0]))

    code = my_qbob.build()
    print(code)
    test = my_qbob.compile()
    test()

    with open(file_location(1)) as f:
        print(f.read())

    with open(file_location(2)) as f:
        print(f.read())

    with open(file_location(3)) as f:
        print(f.read())


def test_debug_new(tmp_path):    
    my_qbob = qbob.OperationBuilder("TestDumpMachine", debug=True)
    my_qbob += Message("Hi from QBOB!")
    
    with my_qbob.allocate_qubits("q", 3) as q:
        my_qbob += H(q[0])
        my_qbob.log_state(q[0])
        my_qbob += H(q[1])
        my_qbob.log_state(q[1])
        my_qbob += X(q[2])
        my_qbob.log_state(q[2])
        my_qbob.returns([M(q[0]), M(q[1]), M(q[2])])

    code = my_qbob.build() # code contains the state at each line
    print(code)
    test = my_qbob.compile()
    test()
