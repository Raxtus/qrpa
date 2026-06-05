from bqskit import compile as bq_compile
from bqskit.ir.lang.qasm2 import OPENQASM2Language

from quantum_transpile_test_suite import (
    QuantumTranspilerTestSuite,
    SingleRunStatistics,
)


class BQSKitTranspilerTestSuite(QuantumTranspilerTestSuite):
    def __init__(self):
        self.sdk_name = "BQSKit"

    def _extract_qubit_count(self, qasm_code: str) -> int:
        return self.import_qasm(qasm_code).num_qudits

    def import_qasm(self, qasm_code: str):
        return OPENQASM2Language().decode(qasm_code)

    def transpile(self, circuit):
        return bq_compile(circuit)

    def verify_circuit(self, original, transpiled) -> bool:
        return True

    def get_circuit_metrics(
            self,
            stats: SingleRunStatistics,
            original,
            transpiled,
    ):
        stats.circuit_width = transpiled.num_qudits

        stats.original_gate_count = original.num_operations
        stats.transpiled_gate_count = transpiled.num_operations

        stats.depth_transpiled = transpiled.depth
