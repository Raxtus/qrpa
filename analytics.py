import os
import json
import pandas as pd
import statistics
import matplotlib.pyplot as plt
from collections import Counter


path = "./experiments/analysis"
directories = os.listdir(path)
folder_paths = [os.path.join(path, name) for name in directories if os.path.isdir(os.path.join(path, name))]

print(folder_paths)

for folder_path in folder_paths:
    json_data_list = []
    # Load all JSON files
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                json_data_list.append(data)

    rows = []

    # Process each record
    for data in json_data_list:
        for record in data:
            algorithm = record["algorithm"].rsplit("_", 1)[0]
            qubits = int(record["algorithm"].rsplit("_", 1)[1])
            sdk = record["sdk_name"]
            runs = record["runs_stats"]
            avg_time = record["timing_metrics"]["avg_transpilation_time_ms"]
            if runs:
                max_time = max(run["transpilation_time_ms"] for run in runs)
                min_time = min(run["transpilation_time_ms"] for run in runs)
                mid_time = statistics.median(run["transpilation_time_ms"] for run in runs)
            else:
                max_time = 0
                min_time = 0
                mid_time = 0

            equiv_counter = Counter(run["equivalent"]["equivalence"] for run in runs)

            rows.append({
                "algorithm": algorithm,
                "sdk": sdk,
                "qubits": qubits,
                "avg_time": avg_time,
                "mid_time": mid_time,
                "min_time": min_time,
                "max_time": max_time,
                "equivalency": equiv_counter,
            })

    df = pd.DataFrame(rows)

    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    SDK_COLOR_MAP = {}


    def get_sdk_color(_sdk_name):
        _sdk_name = _sdk_name.split('_')[0]
        if _sdk_name not in SDK_COLOR_MAP:
            SDK_COLOR_MAP[_sdk_name] = colors[len(SDK_COLOR_MAP) % len(colors)]
        return SDK_COLOR_MAP[_sdk_name]

    grouped = df.sort_values(['algorithm', 'sdk', 'qubits'])
    algorithms = grouped['algorithm'].unique()

    for algo in algorithms:
        plt.figure(figsize=(10, 6))

        subset = grouped[grouped['algorithm'] == algo]

        for sdk_name in subset['sdk'].unique():
            sdk_data = subset[subset['sdk'] == sdk_name]
            color = get_sdk_color(sdk_name)

            # avg
            plt.scatter(
                sdk_data['qubits'],
                sdk_data['avg_time'],
                color=color,
                s=60,
                label=sdk_name
            )

            plt.scatter(
                sdk_data['qubits'],
                sdk_data['min_time'],
                marker="v",
                color=color,
                s=60,
            )

            plt.scatter(
                sdk_data['qubits'],
                sdk_data['max_time'],
                color=color,
                marker="^",
                s=60,
            )

            plt.plot(
                sdk_data['qubits'],
                sdk_data['avg_time'],
                color=color,
                alpha=0.4
            )

        plt.title(f'Algorithm: {algo}')
        plt.xlabel('Number of qubits')
        plt.ylabel('Time (ms)')
        plt.grid(True)
        plt.legend(title="SDK")
        plt.tight_layout()
        plt.show()
