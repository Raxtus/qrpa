import pennylane as qml


from SDKs.pennylane_independent import PennyLaneTranspilerTestSuite


class PennyLaneMappedTranspilerTestSuite(PennyLaneTranspilerTestSuite):

    def __init__(self, sdk_name, gateset, coupling_map):
        super().__init__(sdk_name)
        self.gateset = gateset
        self.coupling_map = coupling_map


    def transpile(self, circuit):
        circuit, fn = qml.transforms.decompose(circuit,gate_set=self.gateset)
        circuit, fn = qml.transforms.transpile(circuit[0],self.coupling_map)
        compiled, fn = qml.compile(circuit[0], basis_set=self.gateset)
        return compiled[0]
