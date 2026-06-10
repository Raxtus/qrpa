import pennylane as qml
from qiskit import qasm2
from functools import partial

from quantum_transpile_test_suite import QuantumTranspilerTestSuite, SingleRunStatistics


class PennyLaneTranspilerTestSuite(QuantumTranspilerTestSuite):

    def _extract_qubit_count(self, qasm_code: str) -> int:
        qc = qasm2.loads(qasm_code)
        self.width = qc.num_qubits
        return qc.num_qubits

    def __init__(self,sdk_name):
        self.pipeline = [
            qml.transforms.decompose,
            partial(qml.transforms.cancel_inverses, recursive=True),
            qml.transforms.merge_rotations,
            qml.transforms.single_qubit_fusion,
        ]
        self.sdk_name = sdk_name

    def import_qasm(self, qasm_code: str):
        return qml.from_qasm(qasm_code)

    def transpile(self, circuit):
        return qml.compile(
            circuit,
            pipeline=self.pipeline,
            num_passes=1
        )

    def verify_circuit(self, original, transpiled) -> bool:
        # TODO
        return True

    def get_circuit_metrics(
            self,
            stats: SingleRunStatistics,
            original,
            transpiled):


        stats.circuit_width = 0

        stats.original_gate_count = 0

        stats.transpiled_gate_count = 0

        stats.depth_transpiled = 0