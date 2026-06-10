from bqskit import compile
from .bqskit_independent import BQSKitTranspilerTestSuite




class BQSKitTargetedTranspilerTestSuite(BQSKitTranspilerTestSuite):
    def __init__(self, sdk_name, gateset):
        super().__init__(sdk_name)
        self.gateset = gateset


    def transpile(self, circuit):
        return compile(circuit, gate_set=self.gateset, with_mapping=False, max_synthesis_size=6)

