from pytket import Circuit
from pytket.qasm import circuit_from_qasm_str
from pytket.passes import SequencePass, DecomposeBoxes, RemoveRedundancies

from quantum_transpile_test_suite import QuantumTranspilerTestSuite, SingleRunStatistics


class PyTKETIndependentTranspilerTestSuite(QuantumTranspilerTestSuite):
    def _extract_qubit_count(self, qasm_code: str) -> int:
        return self.import_qasm(qasm_code).n_qubits

    def __init__(self):
        self.sdk_name = "pytket_independent"

    def import_qasm(self, qasm_code: str) -> Circuit:
        return circuit_from_qasm_str(qasm_code)

    def transpile(self, circuit: Circuit) -> Circuit:
        compiled = circuit.copy()

        basic_pass = SequencePass([DecomposeBoxes(), RemoveRedundancies()])
        basic_pass.apply(compiled)
        return compiled

    def verify_circuit(self, original: Circuit, transpiled: Circuit) -> bool:
        # TODO
        return True

    def get_circuit_metrics(self, stats: SingleRunStatistics, original: Circuit, transpiled: Circuit):
        # Set circuit width (number of qubits)
        stats.circuit_width = transpiled.n_qubits
        # Gate counts
        stats.original_gate_count = original.n_gates
        stats.transpiled_gate_count = transpiled.n_gates
        # Depth of transpiled circuit
        stats.depth_transpiled = transpiled.depth()