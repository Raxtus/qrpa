import pennylane as qml

from qiskit import QuantumCircuit

from pennylane.tape import QuantumScript

from quantum_transpile_test_suite import QuantumTranspilerTestSuite, SingleRunStatistics
from mqt import qcec
from mqt.qcec.pyqcec import EquivalenceCheckingManager


class PennyLaneTranspilerTestSuite(QuantumTranspilerTestSuite):

    def _extract_qubit_count(self, qasm_code: str) -> int:
        return self.import_qasm(qasm_code).num_wires

    def __init__(self, sdk_name):
        self.sdk_name = sdk_name

    def import_qasm(self, qasm_code: str):
        with qml.queuing.AnnotatedQueue() as q:
            qml.from_qasm(qasm_code)()
        return QuantumScript.from_queue(q)

    def transpile(self, circuit):
        compiled, fn = qml.compile(circuit,basis_set={})
        return compiled[0]

    def verify_circuit(self, original, transpiled) -> EquivalenceCheckingManager.Results:
        qc1 = QuantumCircuit.from_qasm_str(qml.to_openqasm(original))
        qc2 = QuantumCircuit.from_qasm_str(qml.to_openqasm(transpiled))
        return qcec.verify(qc1, qc2)

    def get_circuit_metrics(
            self,
            stats: SingleRunStatistics,
            original,
            transpiled):
        t = qml.resource.resources_from_tape(transpiled)

        stats.circuit_width = transpiled.num_wires
        stats.original_gate_count = t.num_gates

        stats.transpiled_gate_count = t.num_gates

        # Depth of circuit
        stats.depth_transpiled = t.depth

        # Gate types with counts
        stats.transpiled_exact_gates = t.gate_types
