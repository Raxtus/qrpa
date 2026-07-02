import json
from datetime import datetime



from SDKs.bqskit_independent import BQSKitTranspilerTestSuite
from SDKs.bqskit_mapped import BQSKitMappedTranspilerTestSuite
from SDKs.bqskit_targeted import BQSKitTargetedTranspilerTestSuite


from SDKs.pennylane_independent import PennyLaneTranspilerTestSuite
from SDKs.pennylane_mapped import PennyLaneMappedTranspilerTestSuite
from SDKs.pennylane_targeted import PennyLaneTargetedTranspilerTestSuite

import pennylane as qml

from SDKs.pytket_independent import PyTKETIndependentTranspilerTestSuite
from SDKs.pytket_targeted import PyTKETTargetedTranspilerTestSuite
from SDKs.pytket_mapped import PyTKETMappedTranspilerTestSuite
from pytket.circuit import OpType
from pytket.architecture import Architecture

from SDKs.qiskit_independent import QiskitIndependentTranspilerTestSuite
from SDKs.qiskit_targeted import QiskitTargetedTranspilerTestSuite
from SDKs.qiskit_mapped import QiskitMappedTranspilerTestSuite
from qiskit.transpiler import CouplingMap

from SDKs.seed import seed

import os
os.environ["QISKIT_TRANSPILER_SEED"] = seed



# Import your SDK implementations


def main():
    output_file = "final/transpiler_results.json"
    max_runs = 5
    max_qubit = 8 # machine model must be set in bqskit

    qiskit_ibm_falcon_gate_set = ["id", "x", "sx", "rz", "cx"]
    qiskit_quantinuum_gate_set = ["rzz", "rz", "ry", "rx"]

    pennylane_ibm_falcon_gate_set = {qml.Identity, qml.X, qml.SX, qml.RZ, qml.CNOT}
    pennylane_ibm_quantinuum_gate_set = [qml.IsingZZ, qml.RZ, qml.RY, qml.RX]

    pytket_ibm_falcon_gate_set = {OpType.noop, OpType.X, OpType.SX, OpType.Rz, OpType.CX}
    pytket_quantinuum_gate_set = {OpType.ZZPhase, OpType.Rz, OpType.Ry, OpType.Rx}

    all_to_all_coupling_map = [(i, j) for i in range(max_qubit) for j in range(i + 1, max_qubit)]
    line_coupling_map = [(i, i + 1) for i in range(max_qubit - 1)]

    from bqskit.ir.gates.parameterized import RZZGate, RZGate, RYGate, RXGate
    from bqskit.ir.gates import IdentityGate, XGate, SXGate, CXGate


    bqskit_ibm_falcon_gate_set = {IdentityGate(), XGate(), SXGate(), RZGate(), CXGate()}
    bqskit_quantinuum_gate_set = {RZZGate(), RZGate(), RYGate(), RXGate()}


    #logging.basicConfig(level=logging.DEBUG)

    sdk_list = [
        {
            "name": "Qiskit_independent",
            "class": QiskitIndependentTranspilerTestSuite,
        },
        {
            "name": "Qiskit_targeted_IBM_gateset",
            "gateset": qiskit_ibm_falcon_gate_set,
            "class": QiskitTargetedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_targeted_Quantinuum_gateset",
            "gateset": qiskit_quantinuum_gate_set,
            "class": QiskitTargetedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_all_to_all_IBM_gateset",
            "gateset": qiskit_ibm_falcon_gate_set,
            "map": CouplingMap.from_full(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_line_IBM_gateset",
            "gateset": qiskit_ibm_falcon_gate_set,
            "map": CouplingMap.from_line(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_all_to_all_Quantinuum_gateset",
            "gateset": qiskit_quantinuum_gate_set,
            "map": CouplingMap.from_full(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_line_Quantinuum_gateset",
            "gateset": qiskit_quantinuum_gate_set,
            "map": CouplingMap.from_line(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Pytket_independent",
            "class": PyTKETIndependentTranspilerTestSuite,
        },
        {
            "name": "Pytket_Targeted_IBM_gateset",
            "gateset": pytket_ibm_falcon_gate_set,
            "class": PyTKETTargetedTranspilerTestSuite,
        },
        {
            "name": "Pytket_Targeted_Quantinuum_gateset",
            "gateset": pytket_quantinuum_gate_set,
            "class": PyTKETTargetedTranspilerTestSuite,
        },
        {
            "name": "Pytket_Mapped_all_to_all_IBM_gateset",
            "gateset": pytket_ibm_falcon_gate_set,
            "map": Architecture(all_to_all_coupling_map),
            "class": PyTKETMappedTranspilerTestSuite,
        },
        {
            "name": "Pytket_Mapped_line_IBM_gateset",
            "gateset": pytket_ibm_falcon_gate_set,
            "map": Architecture(line_coupling_map),
            "class": PyTKETMappedTranspilerTestSuite
        },
        {
            "name": "Pytket_Mapped_all_to_all_Quantinuum_gateset",
            "gateset": pytket_quantinuum_gate_set,
            "map": Architecture(all_to_all_coupling_map),
            "class": PyTKETMappedTranspilerTestSuite,
        },
        {
            "name": "Pytket_Mapped_line_Quantinuum_gateset",
            "gateset": pytket_quantinuum_gate_set,
            "map": Architecture(line_coupling_map),
            "class": PyTKETMappedTranspilerTestSuite,
        },

        {
            "name": "BQSkit_mapped_all_to_all_Quantinuum_gateset",
            "class": BQSKitMappedTranspilerTestSuite,
            "gateset": bqskit_quantinuum_gate_set,
            "map": all_to_all_coupling_map
        },
        {
            "name": "BQSkit_Targeted_Quantinuum_gateset",
            "class": BQSKitTargetedTranspilerTestSuite,
            "gateset": bqskit_quantinuum_gate_set
        },
        {
            "name": "BQSkit_mapped_line_Quantinuum_gateset",
            "class": BQSKitMappedTranspilerTestSuite,
            "gateset": bqskit_quantinuum_gate_set,
            "map": line_coupling_map
        },

        {
            "name": "BQSkit_mapped_all_to_all_IBM_gateset",
            "class": BQSKitMappedTranspilerTestSuite,
            "gateset": bqskit_ibm_falcon_gate_set,
            "map": all_to_all_coupling_map
        },
        {
            "name": "BQSkit_independent",
            "class": BQSKitTranspilerTestSuite,
        },
        {
            "name": "BQSkit_Targeted_IBM_gateset",
            "class": BQSKitTargetedTranspilerTestSuite,
            "gateset": bqskit_ibm_falcon_gate_set
        },

        {
            "name": "BQSkit_mapped_line_IBM_gateset",
            "class": BQSKitMappedTranspilerTestSuite,
            "gateset": bqskit_ibm_falcon_gate_set,
            "map": line_coupling_map
        },

        {
            "name": "Pennylane_independent",
            "class": PennyLaneTranspilerTestSuite,
        },
        {
            "name": "Pennylane_targeted_IBM_gateset",
            "gateset": pennylane_ibm_falcon_gate_set,
            "class": PennyLaneTargetedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_targeted_Quantinuum_gateset",
            "gateset": pennylane_ibm_quantinuum_gate_set,
            "class": PennyLaneTargetedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_mapped_all_to_all_IBM_gateset",
            "gateset": pennylane_ibm_falcon_gate_set,
            "map": all_to_all_coupling_map,
            "class": PennyLaneMappedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_mapped_line_IBM_gateset",
            "gateset": pennylane_ibm_falcon_gate_set,
            "map": line_coupling_map,
            "class": PennyLaneMappedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_mapped_all_to_all_Quantinuum_gateset",
            "gateset": pennylane_ibm_quantinuum_gate_set,
            "map": all_to_all_coupling_map,
            "class": PennyLaneMappedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_mapped_line_Quantinuum_gateset",
            "gateset": pennylane_ibm_quantinuum_gate_set,
            "map": line_coupling_map,
            "class": PennyLaneMappedTranspilerTestSuite,
        },
    ]

    # Initialize SDKs
    sdk_list_r = [
        {
            "name": "Qiskit_independent",
            "class": QiskitIndependentTranspilerTestSuite,
        },
        {
            "name": "Qiskit_targeted_IBM_gateset",
            "gateset": qiskit_ibm_falcon_gate_set,
            "class": QiskitTargetedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_targeted_Quantinuum_gateset",
            "gateset": qiskit_quantinuum_gate_set,
            "class": QiskitTargetedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_all_to_all_IBM_gateset",
            "gateset": qiskit_ibm_falcon_gate_set,
            "map": CouplingMap.from_full(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_line_IBM_gateset",
            "gateset": qiskit_ibm_falcon_gate_set,
            "map": CouplingMap.from_line(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_all_to_all_Quantinuum_gateset",
            "gateset": qiskit_quantinuum_gate_set,
            "map": CouplingMap.from_full(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_line_Quantinuum_gateset",
            "gateset": qiskit_quantinuum_gate_set,
            "map": CouplingMap.from_line(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Pytket_independent",
            "class": PyTKETIndependentTranspilerTestSuite,
        },
        {
            "name": "Pytket_Targeted_IBM_gateset",
            "gateset": pytket_ibm_falcon_gate_set,
            "class": PyTKETTargetedTranspilerTestSuite,
        },
        {
            "name": "Pytket_Targeted_Quantinuum_gateset",
            "gateset": pytket_quantinuum_gate_set,
            "class": PyTKETTargetedTranspilerTestSuite,
        },
        {
            "name": "Pytket_Mapped_all_to_all_IBM_gateset",
            "gateset": pytket_ibm_falcon_gate_set,
            "map": Architecture(all_to_all_coupling_map),
            "class": PyTKETMappedTranspilerTestSuite,
        },
        {
            "name": "Pytket_Mapped_line_IBM_gateset",
            "gateset": pytket_ibm_falcon_gate_set,
            "map": Architecture(line_coupling_map),
            "class": PyTKETMappedTranspilerTestSuite
        },
        {
            "name": "Pytket_Mapped_all_to_all_Quantinuum_gateset",
            "gateset": pytket_quantinuum_gate_set,
            "map": Architecture(all_to_all_coupling_map),
            "class": PyTKETMappedTranspilerTestSuite,
        },
        {
            "name": "Pytket_Mapped_line_Quantinuum_gateset",
            "gateset": pytket_quantinuum_gate_set,
            "map": Architecture(line_coupling_map),
            "class": PyTKETMappedTranspilerTestSuite,
        },

        {
            "name": "BQSkit_mapped_all_to_all_Quantinuum_gateset",
            "class": BQSKitMappedTranspilerTestSuite,
            "gateset": bqskit_quantinuum_gate_set,
            "map": all_to_all_coupling_map
        },
        {
            "name": "BQSkit_Targeted_Quantinuum_gateset",
            "class": BQSKitTargetedTranspilerTestSuite,
            "gateset": bqskit_quantinuum_gate_set
        },
        {
            "name": "BQSkit_mapped_line_Quantinuum_gateset",
            "class": BQSKitMappedTranspilerTestSuite,
            "gateset": bqskit_quantinuum_gate_set,
            "map": line_coupling_map
        },

        {
            "name": "BQSkit_mapped_all_to_all_IBM_gateset",
            "class": BQSKitMappedTranspilerTestSuite,
            "gateset": bqskit_ibm_falcon_gate_set,
            "map": all_to_all_coupling_map
        },
        {
            "name": "BQSkit_independent",
            "class": BQSKitTranspilerTestSuite,
        },
        {
            "name": "BQSkit_Targeted_IBM_gateset",
            "class": BQSKitTargetedTranspilerTestSuite,
            "gateset": bqskit_ibm_falcon_gate_set
        },

        {
            "name": "BQSkit_mapped_line_IBM_gateset",
            "class": BQSKitMappedTranspilerTestSuite,
            "gateset": bqskit_ibm_falcon_gate_set,
            "map": line_coupling_map
        },

        {
            "name": "Pennylane_independent",
            "class": PennyLaneTranspilerTestSuite,
        },
        {
            "name": "Pennylane_targeted_IBM_gateset",
            "gateset": pennylane_ibm_falcon_gate_set,
            "class": PennyLaneTargetedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_targeted_Quantinuum_gateset",
            "gateset": pennylane_ibm_quantinuum_gate_set,
            "class": PennyLaneTargetedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_mapped_all_to_all_IBM_gateset",
            "gateset": pennylane_ibm_falcon_gate_set,
            "map": all_to_all_coupling_map,
            "class": PennyLaneMappedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_mapped_line_IBM_gateset",
            "gateset": pennylane_ibm_falcon_gate_set,
            "map": line_coupling_map,
            "class": PennyLaneMappedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_mapped_all_to_all_Quantinuum_gateset",
            "gateset": pennylane_ibm_quantinuum_gate_set,
            "map": all_to_all_coupling_map,
            "class": PennyLaneMappedTranspilerTestSuite,
        },
        {
            "name": "Pennylane_mapped_line_Quantinuum_gateset",
            "gateset": pennylane_ibm_quantinuum_gate_set,
            "map": line_coupling_map,
            "class": PennyLaneMappedTranspilerTestSuite,
        },

    ]

    algorithms = ["qaoa", "qft", "hhl", "randomcircuit","grover","vqe_real_amp"]

    test_list = [
        f"./benchmark/{algorithm}_{i:02d}.qasm"
        for algorithm in algorithms
        for i in range(2, max_qubit + 1)
    ]

    for sdk in sdk_list:
        sdk_name = sdk["name"]
        print(f"Processing SDK: {sdk_name}")
        suite_class = sdk["class"]
        if "gateset" in sdk:
            if "map" in sdk:
                suite = suite_class(sdk_name, sdk["gateset"], sdk["map"])
            else:
                suite = suite_class(sdk_name, sdk["gateset"])
        else:
            suite = suite_class(sdk_name)

        results_for_sdk = []


        for file in test_list:
            if file.endswith(".qasm"):
                stats = suite.test(file, max_runs)
                stats_dict = stats.to_dict()
                results_for_sdk.append(stats_dict)

        # Save to JSON with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"{output_file.rstrip('.json')}_{timestamp}_{sdk_name}.json"
        with open(output_path, "w") as f:
            json.dump(results_for_sdk, f, indent=4)


        print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
