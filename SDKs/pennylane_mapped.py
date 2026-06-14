from functools import partial

import pennylane as qml
from sympy import decompose

from SDKs.pennylane_independent import PennyLaneTranspilerTestSuite


class PennyLaneMappedTranspilerTestSuite(PennyLaneTranspilerTestSuite):

    def __init__(self, sdk_name, gateset, coupling_map):
        super().__init__(sdk_name)
        self.gateset = gateset
        self.coupling_map = coupling_map
        self.pipeline = qml.transform(
            partial(qml.transforms.decompose,gate_set=self.gateset),
            partial(qml.transforms.transpile,coupling_map=self.coupling_map),
            partial(qml.transforms.decompose,gate_set=self.gateset),
            qml.transforms.commute_controlled,
            qml.transforms.cancel_inverses,
            qml.transforms.merge_rotations,
            qml.transforms.remove_barrier)

    def transpile(self, circuit):
        compiled, fn = qml.compile(circuit, basis_set=self.gateset, pipeline=self.pipeline)
        return compiled[0]
