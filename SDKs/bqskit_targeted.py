from bqskit import compile, MachineModel

from .bqskit_independent import BQSKitTranspilerTestSuite

class BQSKitTargetedTranspilerTestSuite(BQSKitTranspilerTestSuite):
    def __init__(self, sdk_name, gateset):
        super().__init__(sdk_name)
        self.model = MachineModel(32,gate_set=gateset)


    def transpile(self, circuit):
        return compile(circuit, model=self.model, with_mapping=False, max_synthesis_size=4)

