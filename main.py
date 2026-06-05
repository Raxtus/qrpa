import json
from datetime import datetime

from SDKs.pennylane_independent import PennyLaneTranspilerTestSuite
from SDKs.pytket_independent import PyTKETIndependentTranspilerTestSuite
from SDKs.qiskit_independent import QiskitIndependentTranspilerTestSuite



# Import your SDK implementations
# from your_module import QiskitTranspilerTestSuite, RunStatistics

# Assuming the classes are defined in the same file or imported accordingly
# For this example, I will assume they are already imported or defined above

def main():
    output_file = "transpiler_results.json"

    # Initialize SDKs
    sdk_list = [
        {
            "name": "Qiskit_independent",
            "class": QiskitIndependentTranspilerTestSuite,
        },
        {
            "name": "Pytket_independent",
            "class": PyTKETIndependentTranspilerTestSuite,
        }
    ]

    test_list = ["./benchmark/grover_02.qasm","./benchmark/grover_03.qasm"]

    all_results = {}

    for sdk in sdk_list:
        sdk_name = sdk["name"]
        print(f"Processing SDK: {sdk_name}")
        suite_class = sdk["class"]
        suite = suite_class()
        suite.sdk_name = sdk_name

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
