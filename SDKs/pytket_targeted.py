from pytket import Circuit
from pytket.extensions.qiskit import qiskit_convert
from pytket import qasm
from mqt.qcec.pyqcec import EquivalenceCheckingManager
from mqt import qcec

from pytket.passes import DecomposeBoxes, SequencePass, FullPeepholeOptimise, KAKDecomposition, CliffordSimp ,SynthesiseTket,AutoRebase, RemoveRedundancies

from .pytket_independent import PyTKETIndependentTranspilerTestSuite


class PyTKETTargetedTranspilerTestSuite(PyTKETIndependentTranspilerTestSuite):

    def __init__(self, sdk_name, gateset):
        super().__init__(sdk_name)
        self.gateset = gateset

    def transpile(self, circuit: Circuit) -> Circuit:
        compiled = circuit.copy()

        basic_pass = SequencePass([
            DecomposeBoxes(),
            FullPeepholeOptimise(allow_swaps=False),
            KAKDecomposition(allow_swaps=False),
            CliffordSimp(allow_swaps=False),
            SynthesiseTket(),
            AutoRebase(self.gateset),
            RemoveRedundancies()])
        basic_pass.apply(compiled)
        return compiled