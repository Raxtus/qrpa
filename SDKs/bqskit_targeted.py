from bqskit import MachineModel
from bqskit.compiler import Workflow

from .bqskit_independent import BQSKitTranspilerTestSuite

from bqskit.passes import ExtractMeasurements, UnfoldPass, SetRandomSeedPass, RestoreMeasurements

from bqskit.passes.mapping.setmodel import SetModelPass
from bqskit.compiler.compile import build_multi_qudit_retarget_workflow, build_gate_deletion_optimization_workflow
from bqskit.compiler.compile import build_single_qudit_retarget_workflow
from bqskit.compiler.compile import build_sabre_mapping_workflow
from bqskit.passes.util.log import LogErrorPass
from bqskit.passes.mapping.apply import ApplyPlacement


class BQSKitTargetedTranspilerTestSuite(BQSKitTranspilerTestSuite):
    def __init__(self, sdk_name, gateset):
        super().__init__(sdk_name)
        self.gateset = gateset

    def transpile(self, circuit):
        model = MachineModel(circuit.num_qudits, gate_set=self.gateset)

        workflow = Workflow([
            SetRandomSeedPass(),
            UnfoldPass(),
            ExtractMeasurements(),

            # Core optimization level 2
            SetModelPass(model=model),
            build_multi_qudit_retarget_workflow(2, max_synthesis_size=self.max_synthesis_size),
            # We abandon mapping
            # build_sabre_mapping_workflow()
            # Unnecessary because no sabre
            # build_multi_qudit_retarget_workflow(2, synthesis_epsilon, max_synthesis_size, error_threshold, error_sim_size),
            build_single_qudit_retarget_workflow(2, max_synthesis_size=self.max_synthesis_size),

            build_gate_deletion_optimization_workflow(2, max_synthesis_size=self.max_synthesis_size),

            LogErrorPass(),
            ApplyPlacement(),
            RestoreMeasurements()
        ])

        compiled = self.compiler.compile(circuit, workflow)
        return compiled
