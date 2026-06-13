from bqskit import compile, MachineModel

from .bqskit_independent import BQSKitTranspilerTestSuite


class BQSKitMappedTranspilerTestSuite(BQSKitTranspilerTestSuite):

    def __init__(self, sdk_name, gateset, coupling_map):
        super().__init__(sdk_name)
        self.model = MachineModel(32, coupling_graph=coupling_map, gate_set=gateset)

    def transpile(self, circuit):
        return compile(circuit, model=self.model, max_synthesis_size=4,num_workers=1)
