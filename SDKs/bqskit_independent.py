from bqskit import compile
from bqskit.ext import bqskit_to_qiskit
from bqskit.ir.lang.qasm2 import OPENQASM2Language

from mqt import qcec
from mqt.qcec.pyqcec import EquivalenceCheckingManager

from quantum_transpile_test_suite import (
    QuantumTranspilerTestSuite,
    SingleRunStatistics,
)


class BQSKitTranspilerTestSuite(QuantumTranspilerTestSuite):
    def __init__(self, sdk_name):
        self.sdk_name = sdk_name

    def _extract_qubit_count(self, qasm_code: str) -> int:
        return self.import_qasm(qasm_code).num_qudits

    def import_qasm(self, qasm_code: str):
        return OPENQASM2Language().decode(qasm_code)

    def transpile(self, circuit):
        return compile(circuit, model=None, with_mapping=False, max_synthesis_size=4)

    def verify_circuit(self, original,
                       transpiled) -> EquivalenceCheckingManager.Results:
        return qcec.verify(bqskit_to_qiskit(original), bqskit_to_qiskit(transpiled))

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
