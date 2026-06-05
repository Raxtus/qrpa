import pennylane as qml
from pennylane.transforms import decompose

from quantum_transpile_test_suite import QuantumTranspilerTestSuite, SingleRunStatistics


class PennyLaneTranspilerTestSuite(QuantumTranspilerTestSuite):
    def _extract_qubit_count(self, qasm_code: str) -> int:
        circuit = self.import_qasm(qasm_code)
        return circuit.num_wires

    def __init__(self):
        self.sdk_name = "PennyLane"

    def import_qasm(self, qasm_code: str):
        qml.from_qasm(qasm_code)()
        return qml.probs()

    def transpile(self, circuit):
        # PennyLane uses transforms for optimization
        # Decompose circuit to native gates
        return qml.compile(circuit)

    def verify_circuit(self, original, transpiled) -> bool:
        # TODO
        return True

    def get_circuit_metrics(
            self,
            stats: SingleRunStatistics,
            original,
            transpiled):
        # Set circuit width (number of qubits)
        stats.circuit_width = transpiled.num_wires
        # Gate counts
        stats.original_gate_count = len(original.operations)
        stats.transpiled_gate_count = len(transpiled.operations)
        # Depth estimation
        stats.depth_transpiled = len(transpiled.tape.graph.layers)
