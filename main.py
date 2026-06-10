import json
from datetime import datetime

from qiskit.transpiler import CouplingMap

from bqskit.ext import model_from_backend
from cirq.ops.gateset_test import gateset

from SDKs.bqskit_independent import BQSKitTranspilerTestSuite
from SDKs.pennylane_independent import PennyLaneTranspilerTestSuite
from SDKs.pytket_independent import PyTKETIndependentTranspilerTestSuite
from SDKs.qiskit_independent import QiskitIndependentTranspilerTestSuite
from SDKs.qiskit_targeted import QiskitTargetedTranspilerTestSuite
from SDKs.qiskit_mapped import QiskitMappedTranspilerTestSuite


# Import your SDK implementations
# from your_module import QiskitTranspilerTestSuite, RunStatistics

# Assuming the classes are defined in the same file or imported accordingly
# For this example, I will assume they are already imported or defined above

def main():
    output_file = "transpiler_results.json"

    max_qubit = 4



    # Initialize SDKs
    sdk_list = [
        {
            "name": "Qiskit_independent",
            "class": QiskitIndependentTranspilerTestSuite,
        },
        {
            "name": "Qiskit_targeted_IBM_gateset",
            "gateset": ["rz", "sx", "x", "cx"],
            "class": QiskitTargetedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_targeted_Quantinuum_gateset",
            "gateset": ["rzz", "rz", "ry", "rx"],
            "class": QiskitTargetedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_all_to_all_IBM_gateset",
            "gateset": ["rz", "sx", "x", "cx"],
            "map": CouplingMap.from_full(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_line_IBM_gateset",
            "gateset": ["rz", "sx", "x", "cx"],
            "map": CouplingMap.from_line(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_all_to_all_Quantinuum_gateset",
            "gateset": ["rzz", "rz", "ry", "rx"],
            "map": CouplingMap.from_full(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        {
            "name": "Qiskit_mapped_line_Quantinuum_gateset",
            "gateset": ["rzz", "rz", "ry", "rx"],
            "map": CouplingMap.from_line(max_qubit),
            "class": QiskitMappedTranspilerTestSuite,
        },
        #{
        #    "name": "Pennylane_independent",
        #    "class": PennyLaneTranspilerTestSuite,
        #},
        #{
        #   "name": "BQSkit_independent",
        #    "class": BQSKitTranspilerTestSuite,
        #},
        #{
        #    "name": "Pytket_independent",
        #    "class": PyTKETIndependentTranspilerTestSuite,
        #},




    ]

    algorithms = ["grover", "hhl", "qaoa", "qft", "randomcircuit", "vqe_real_amp"]

    test_list = [
        f"./benchmark/{algorithm}_{i:02d}.qasm"
        for algorithm in algorithms
        for i in range(2, max_qubit + 1)
    ]

    all_results = {}

    #independent
    for sdk in sdk_list:
        sdk_name = sdk["name"]
        print(f"Processing SDK: {sdk_name}")
        suite_class = sdk["class"]
        if "gateset" in sdk:
            if "map" in sdk:
                suite = suite_class(sdk_name,sdk["gateset"],sdk["map"])
            else:
                suite = suite_class(sdk_name, sdk["gateset"])
        else:
            suite = suite_class(sdk_name)

        results_for_sdk = []

        for file in test_list:
            if file.endswith(".qasm"):
                stats = suite.test(file)
                stats_dict = stats.to_dict()
                results_for_sdk.append(stats_dict)

        all_results[sdk_name] = results_for_sdk

        # Save to JSON with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"{output_file.rstrip('.json')}_{timestamp}.json"
        with open(output_path, "w") as f:
            json.dump(all_results, f, indent=4)

        print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
