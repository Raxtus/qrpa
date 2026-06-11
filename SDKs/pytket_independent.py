from pytket import Circuit
from pytket.extensions.qiskit import qiskit_convert
from pytket import qasm
from mqt.qcec.pyqcec import EquivalenceCheckingManager
from mqt import qcec

from pytket.utils import gate_counts

from pytket.passes import DecomposeBoxes, SequencePass, FullPeepholeOptimise, KAKDecomposition, CliffordSimp ,SynthesiseTket, RemoveRedundancies

from quantum_transpile_test_suite import QuantumTranspilerTestSuite, SingleRunStatistics


class PyTKETIndependentTranspilerTestSuite(QuantumTranspilerTestSuite):
    def _extract_qubit_count(self, qasm_code: str) -> int:
        return self.import_qasm(qasm_code).n_qubits

    def __init__(self,sdk_name):
        self.sdk_name = sdk_name

    def import_qasm(self, qasm_code: str) -> Circuit:
        return qasm.circuit_from_qasm_str(qasm_code, maxwidth=32)

    def transpile(self, circuit: Circuit) -> Circuit:
        compiled = circuit.copy()

        basic_pass = SequencePass([
            DecomposeBoxes(),
            FullPeepholeOptimise(allow_swaps=False),
            KAKDecomposition(allow_swaps=False),
            CliffordSimp(allow_swaps=False),
            SynthesiseTket(),
            RemoveRedundancies()])
        basic_pass.apply(compiled)
        return compiled

    def verify_circuit(self, original: Circuit,
                       transpiled: Circuit) -> EquivalenceCheckingManager.Results:
        return qcec.verify(qiskit_convert.tk_to_qiskit(original), qiskit_convert.tk_to_qiskit(transpiled),check_partial_equivalence=True)

    def get_circuit_metrics(self, stats: SingleRunStatistics, original: Circuit, transpiled: Circuit):
        # Set circuit width (number of qubits)
        stats.circuit_width = transpiled.n_qubits
        # Gate counts
        stats.original_gate_count = original.n_gates
        stats.transpiled_gate_count = transpiled.n_gates
        stats.transpiled_exact_gates = {str(op): count for op, count in gate_counts(transpiled).items()}
        # Depth of transpiled circuit
        stats.depth_transpiled = transpiled.depth()