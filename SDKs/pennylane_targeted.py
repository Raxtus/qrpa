import pennylane as qml

from SDKs.pennylane_independent import PennyLaneTranspilerTestSuite


class PennyLaneTargetedTranspilerTestSuite(PennyLaneTranspilerTestSuite):


    def __init__(self,sdk_name, gateset):
        super().__init__(sdk_name)
        self.gateset = gateset


    def transpile(self, circuit):
        compiled, fn = qml.compile(circuit, basis_set=self.gateset)
        return compiled[0]

