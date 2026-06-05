import qiskit
from qiskit import QuantumCircuit
from qiskit import qasm2

from quantum_transpile_test_suite import QuantumTranspilerTestSuite, SingleRunStatistics


class QiskitIndependentTranspilerTestSuite(QuantumTranspilerTestSuite):
    def _extract_qubit_count(self, qasm_code: str) -> int:
        return self.import_qasm(qasm_code).width()

    def __init__(self):
        self.sdk_name = "Qiskit_independent"

    def import_qasm(self, qasm_code: str) -> QuantumCircuit:
        return qasm2.loads(qasm_code)

    def transpile(self, circuit: QuantumCircuit) -> QuantumCircuit:
        return qiskit.transpile(circuit)

    def verify_circuit(self, original: QuantumCircuit, transpiled: QuantumCircuit) -> bool:
        # TODO
        return True

    def get_circuit_metrics(self, stats: SingleRunStatistics, original: QuantumCircuit, transpiled: QuantumCircuit):
        # Set circuit width
        stats.circuit_width = transpiled.width()
        # Gate counts
        stats.original_gate_count = original.size()
        stats.transpiled_gate_count = transpiled.size()
        # Depth of transpiled circuit
        stats.depth_transpiled = transpiled.depth()