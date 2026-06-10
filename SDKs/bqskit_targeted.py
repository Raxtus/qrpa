from bqskit import compile
from .bqskit_independent import BQSKitTranspilerTestSuite

from quantum_transpile_test_suite import (
    QuantumTranspilerTestSuite,
    SingleRunStatistics,
)


class BQSKitTargetedTranspilerTestSuite(BQSKitTranspilerTestSuite):
    def __init__(self, sdk_name, backend):
        super().__init__(sdk_name)
        self.backend = backend


    def transpile(self, circuit):
        return compile(circuit, model=None, with_mapping=False)

