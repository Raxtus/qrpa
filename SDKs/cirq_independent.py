import cirq
from quantum_transpile_test_suite import QuantumTranspilerTestSuite, SingleRunStatistics


class CirqIndependentTranspilerTestSuite(QuantumTranspilerTestSuite):
    def _extract_qubit_count(self, qasm_code: str) -> int:
        circuit = self.import_qasm(qasm_code)
        return len(circuit.all_qubits())

    def __init__(self):
        self.sdk_name = "Cirq_independent"

    def import_qasm(self, qasm_code: str) -> cirq.Circuit:
        # Import QASM into a Circuit object
        return cirq.from_qasm(qasm_code)

    def transpile(self, circuit: cirq.Circuit) -> cirq.Circuit:
        # Target-independent optimization using default Cirq optimizers
        optimized = cirq.drop_negligible_operations(circuit)
        optimized = cirq.merge_single_qubit_gates(optimized)
        optimized = cirq.eject_z(optimized)
        return optimized

    def verify_circuit(self, original: cirq.Circuit, transpiled: cirq.Circuit) -> bool:
        # TODO
        return True

    def get_circuit_metrics(self, stats: SingleRunStatistics, original: cirq.Circuit, transpiled: cirq.Circuit):
        # Set circuit width (number of qubits)
        stats.circuit_width = len(transpiled.all_qubits())
        # Gate counts
        stats.original_gate_count = len(list(original.all_operations()))
        stats.transpiled_gate_count = len(list(transpiled.all_operations()))
        # Depth of transpiled circuit
        stats.depth_transpiled = len(transpiled)
