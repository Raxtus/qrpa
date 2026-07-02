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

from seed import seed

class BQSKitMappedTranspilerTestSuite(BQSKitTranspilerTestSuite):

    def __init__(self, sdk_name, gateset, coupling_map):
        super().__init__(sdk_name)
        model = MachineModel(8, gate_set=gateset, coupling_graph=coupling_map)
        self.workflow = Workflow([
            SetRandomSeedPass(seed=seed),
            UnfoldPass(),
            ExtractMeasurements(),

            # Core optimization level 2
            SetModelPass(model=model),
            build_multi_qudit_retarget_workflow(2, max_synthesis_size=self.max_synthesis_size),
            build_sabre_mapping_workflow(),

            build_multi_qudit_retarget_workflow(2, max_synthesis_size=self.max_synthesis_size),
            build_single_qudit_retarget_workflow(2, max_synthesis_size=self.max_synthesis_size),

            build_gate_deletion_optimization_workflow(2, max_synthesis_size=self.max_synthesis_size),

            LogErrorPass(),
            ApplyPlacement(),
            RestoreMeasurements()
        ])
