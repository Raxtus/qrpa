
from bqskit.ext import bqskit_to_qiskit
from bqskit.ir.lang.qasm2 import OPENQASM2Language

from bqskit.compiler import Compiler, Workflow
from bqskit import MachineModel
from bqskit.passes import ExtractMeasurements, UnfoldPass, SetRandomSeedPass, RestoreMeasurements


from bqskit.passes.mapping.setmodel import SetModelPass
from bqskit.compiler.compile import build_multi_qudit_retarget_workflow, build_gate_deletion_optimization_workflow
from bqskit.compiler.compile import build_single_qudit_retarget_workflow
from bqskit.compiler.compile import build_sabre_mapping_workflow
from bqskit.passes.util.log import LogErrorPass
from bqskit.passes.mapping.apply import ApplyPlacement

from mqt import qcec
from mqt.qcec.pyqcec import EquivalenceCheckingManager
from qiskit import QuantumCircuit

from quantum_transpile_test_suite import (
    QuantumTranspilerTestSuite,
    SingleRunStatistics,
)



class BQSKitTranspilerTestSuite(QuantumTranspilerTestSuite):
    bqskit_compiler = Compiler(num_workers=1)

    def __init__(self, sdk_name):
        self.sdk_name = sdk_name
        self.max_synthesis_size = 3 # change if you need to. It's default by BQSkit docs
        model = MachineModel(8)
        self.compiler = Compiler(num_workers=1)

        self.workflow = Workflow([
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
            # Additional optimization level 2 pass
            build_gate_deletion_optimization_workflow(2, max_synthesis_size=self.max_synthesis_size),

            LogErrorPass(),
            ApplyPlacement(),
            RestoreMeasurements()
        ])

    def _extract_qubit_count(self, qasm_code: str) -> int:
        return self.import_qasm(qasm_code).num_qudits

    def import_qasm(self, qasm_code: str):
        return OPENQASM2Language().decode(qasm_code)

    def transpile(self, circuit):
            return BQSKitTranspilerTestSuite.bqskit_compiler.compile(circuit, self.workflow)

    def verify_circuit(self, original,
                       transpiled) -> EquivalenceCheckingManager.Results:
        return qcec.verify(QuantumCircuit.from_qasm_str(OPENQASM2Language().encode(original)), QuantumCircuit.from_qasm_str(OPENQASM2Language().encode(transpiled)),check_partial_equivalence=True)

    def get_circuit_metrics(
            self,
            stats: SingleRunStatistics,
            original,
            transpiled,
    ):
        stats.circuit_width = transpiled.num_qudits

        stats.original_gate_count = original.num_operations
        stats.transpiled_gate_count = transpiled.num_operations

        stats.depth_transpiled = transpiled.depth

        stats.transpiled_exact_gates = {str(op): count for op, count in transpiled.gate_counts.items()}

