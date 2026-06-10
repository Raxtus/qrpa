from bqskit import compile
from .bqskit_independent import BQSKitTranspilerTestSuite



class BQSKitMappedTranspilerTestSuite(BQSKitTranspilerTestSuite):

    def __init__(self, sdk_name, gateset, coupling_map):
        super().__init__(sdk_name)
        self.gateset = gateset
        self.coupling_map = coupling_map


    def transpile(self, circuit):
        return compile(circuit, gate_set=self.gateset, coupling_graph=self.coupling_map, max_synthesis_size=6)

