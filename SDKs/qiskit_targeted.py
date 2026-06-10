import qiskit
from qiskit import QuantumCircuit

from .qiskit_independent import QiskitIndependentTranspilerTestSuite



class QiskitTargetedTranspilerTestSuite(QiskitIndependentTranspilerTestSuite):

    def __init__(self, sdk_name,gateset):
        super().__init__(sdk_name)
        self.gateset = gateset

    def transpile(self, circuit: QuantumCircuit) -> QuantumCircuit:
        return qiskit.transpile(
            circuit,
            basis_gates=self.gateset,
            routing_method="none",
            optimization_level=2
        )
