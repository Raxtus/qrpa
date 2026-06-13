import qiskit
from qiskit import QuantumCircuit

from .qiskit_independent import QiskitIndependentTranspilerTestSuite


class QiskitMappedTranspilerTestSuite(QiskitIndependentTranspilerTestSuite):

    def __init__(self, sdk_name, gateset, coupling_map):
        super().__init__(sdk_name)
        self.gateset = gateset
        self.coupling_map = coupling_map

    def transpile(self, circuit: QuantumCircuit) -> QuantumCircuit:
        return qiskit.transpile(
            circuit,
            basis_gates=self.gateset,
            coupling_map=self.coupling_map,
            optimization_level=2
        )
