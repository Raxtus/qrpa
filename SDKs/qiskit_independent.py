import qiskit
from qiskit.circuit import QuantumCircuit

from mqt import qcec
from mqt.qcec.pyqcec import EquivalenceCheckingManager
from qiskit.transpiler.passes import Unroll3qOrMore

from quantum_transpile_test_suite import SingleRunStatistics, QuantumTranspilerTestSuite



class QiskitIndependentTranspilerTestSuite(QuantumTranspilerTestSuite):
    def _extract_qubit_count(self, qasm_code: str) -> int:
        return self.import_qasm(qasm_code).num_qubits

    def __init__(self,sdk_name):
        self.sdk_name = sdk_name

    def import_qasm(self, qasm_code: str) -> QuantumCircuit:
        return  QuantumCircuit.from_qasm_str(qasm_code)

    def transpile(self, circuit: QuantumCircuit) -> QuantumCircuit:
        circuit = Unroll3qOrMore()(circuit)
        return qiskit.transpile(circuit,optimization_level=2,routing_method="none")

    def verify_circuit(self, original: QuantumCircuit, transpiled: QuantumCircuit) -> EquivalenceCheckingManager.Results:
        return qcec.verify(original,transpiled,check_partial_equivalence=True)

    def get_circuit_metrics(self, stats: SingleRunStatistics, original: QuantumCircuit, transpiled: QuantumCircuit):
        # Set circuit width
        stats.circuit_width = transpiled.num_qubits
        # Gate counts
        stats.original_gate_count = original.size()
        stats.transpiled_gate_count = transpiled.size()
        # Depth of transpiled circuit
        stats.depth_transpiled = transpiled.depth()

        stats.transpiled_exact_gates = {str(op): count for op, count in transpiled.count_ops().items()}