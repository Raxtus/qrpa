from pytket import Circuit

from pytket.passes import DecomposeBoxes, SequencePass, FullPeepholeOptimise, KAKDecomposition, CliffordSimp ,SynthesiseTket,AutoRebase, RemoveRedundancies, DefaultMappingPass

from .pytket_independent import PyTKETIndependentTranspilerTestSuite


class PyTKETMappedTranspilerTestSuite(PyTKETIndependentTranspilerTestSuite):


    def __init__(self, sdk_name,gateset, architecture):
        super().__init__(sdk_name)
        self.gateset = gateset
        self.architecture = architecture

    def transpile(self, circuit: Circuit) -> Circuit:
        compiled = circuit.copy()

        basic_pass = SequencePass([
            DecomposeBoxes(),
            FullPeepholeOptimise(allow_swaps=True),
            DefaultMappingPass(self.architecture, delay_measures=True),
            KAKDecomposition(allow_swaps=True),
            CliffordSimp(allow_swaps=True),
            SynthesiseTket(),
            AutoRebase(self.gateset),
            RemoveRedundancies()])
        basic_pass.apply(compiled)
        return compiled