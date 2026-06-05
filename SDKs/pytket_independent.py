from pytket import Circuit
from pytket.qasm import qasm
from pytket.passes import (
    FullPeepholeOptimise,
    RemoveRedundancies,
)

from quantum_transpile_test_suite import QuantumTranspilerTestSuite, SingleRunStatistics


class PyTKETIndependentTranspilerTestSuite(QuantumTranspilerTestSuite):
    def _extract_qubit_count(self, qasm_code: str) -> int:
        return len(self.import_qasm(qasm_code).qubits)

    def __init__(self):
        self.sdk_name = "PyTKET_independent"

    def import_qasm(self, qasm_code: str) -> Circuit:
        return qasm.circuit_from_qasm_str(qasm_code, maxwidth=32)

    def transpile(self, circuit: Circuit) -> Circuit:
        optimized = circuit.copy()
        FullPeepholeOptimise().apply(optimized)
        return optimized

    def verify_circuit(self, original: Circuit, transpiled: Circuit) -> bool:
        # TODO
        return True

    def get_circuit_metrics(self, stats: SingleRunStatistics, original: Circuit, transpiled: Circuit):
        # Set circuit width (number of qubits)
        stats.circuit_width = len(transpiled.qubits)
        # Gate counts
        stats.original_gate_count = len(original.all_commands())
        stats.transpiled_gate_count = len(transpiled.all_commands())
        # Depth of transpiled circuit
        stats.depth_transpiled = transpiled.depth()
