import os
import json
from os import times

import pandas as pd
import statistics
import matplotlib.pyplot as plt
from collections import Counter

from matplotlib.gridspec import GridSpec
from matplotlib.pyplot import figure

path = "./experiments/analysis"
directories = os.listdir(path)
folder_paths = [name for name in directories if os.path.isdir(os.path.join(path, name))]

print(folder_paths)

for folder in folder_paths:
    folder_path = os.path.join(path,folder)
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

            avg_gates = record["circuit_metrics"]["avg_transpiled_gate_count"]
            if runs:
                times = [run["transpilation_time_ms"] for run in runs]
                max_time = max(times)
                min_time = min(times)
                mid_time = statistics.median(times)
                gates = [run["transpiled_gate_count"] for run in runs]
                min_gate = min(gates)
                max_gate = max(gates)
                mid_gate = statistics.median(gates)
                original_gate = statistics.mode(run["original_gate_count"] for run in runs)
            else:
                max_time = 0
                min_time = 0
                mid_time = 0
                min_gate = 0
                max_gate = 0
                mid_gate = 0
                original_gate = 0

            equiv_counter = Counter(run["equivalent"]["equivalence"] for run in runs)

            rows.append({
                "algorithm": algorithm,
                "sdk": sdk,
                "qubits": qubits,
                "avg_time": avg_time,
                "mid_time": mid_time,
                "min_time": min_time,
                "max_time": max_time,
                "min_gate": min_gate,
                "max_gate": max_gate,
                "mid_gate": mid_gate,
                "avg_gate": avg_gates,
                "original_gate": original_gate,
                "equivalency": dict(equiv_counter)
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
        fig = plt.figure(figsize=(14, 14))
        fig.suptitle(algo)

        subset = grouped[grouped['algorithm'] == algo]
        gs = GridSpec(3, max(1, subset['sdk'].unique().size), height_ratios=[3, 3, 2], figure=fig)
        ax_main = fig.add_subplot(gs[0, :])
        ax_gate = fig.add_subplot(gs[1, :])

        for sdk_name in subset['sdk'].unique():
            sdk_data = subset[subset['sdk'] == sdk_name]
            color = get_sdk_color(sdk_name)

            ax_main.scatter(
                sdk_data['qubits'],
                sdk_data['avg_time'],
                color=color,
                s=60,
                label=sdk_name
            )

            ax_main.scatter(
                sdk_data['qubits'],
                sdk_data['min_time'],
                marker="v",
                color=color,
                s=60,
            )

            ax_main.scatter(
                sdk_data['qubits'],
                sdk_data['max_time'],
                color=color,
                marker="^",
                s=60,
            )

            ax_main.scatter(
                sdk_data['qubits'],
                sdk_data['mid_time'],
                color=color,
                marker="x",
                s=60,
            )

            ax_main.plot(
                sdk_data['qubits'],
                sdk_data['avg_time'],
                color=color,
                alpha=0.4
            )

            ax_gate.scatter(
                sdk_data['qubits'],
                sdk_data['avg_gate'],
                color=color,
                s=60,
                label=sdk_name
            )

            ax_gate.scatter(
                sdk_data['qubits'],
                sdk_data['min_gate'],
                marker="v",
                color=color,
                s=60,
            )

            ax_gate.scatter(
                sdk_data['qubits'],
                sdk_data['max_gate'],
                color=color,
                marker="^",
                s=60,
            )

            ax_gate.scatter(
                sdk_data['qubits'],
                sdk_data['mid_gate'],
                color=color,
                marker="x",
                s=60,
            )
            ax_gate.scatter(
                sdk_data['qubits'],
                sdk_data['original_gate'],
                color="gray",
                marker="_",
                s=60,
            )

            ax_gate.plot(
                sdk_data['qubits'],
                sdk_data['avg_gate'],
                color=color,
                alpha=0.4
            )

        ax_main.set_xlabel('Number of qubits')
        ax_main.set_ylabel('Time (ms)')
        ax_main.grid(True)
        ax_main.legend(title="SDK")

        ax_gate.set_xlabel('Number of qubits')
        ax_gate.set_ylabel('Number of gates')
        ax_gate.grid(True)


        all_categories = sorted({
            key
            for d in df["equivalency"]
            for key in d.keys()
        })

        palette = plt.rcParams['axes.prop_cycle'].by_key()['color']

        EQUIV_COLOR_MAP = {'equivalent': '#2ca02c', 'equivalent_up_to_global_phase': '#1f77b4', 'no_information': 'gray', 'not_equivalent': '#d62728'}

        legend_items = {}

        for col, sdk_name in enumerate(subset['sdk'].unique()):
            ax = fig.add_subplot(gs[2, col])


            sdk_data = subset[subset["sdk"] == sdk_name]

            equiv_df = pd.DataFrame(
                sdk_data["equivalency"].tolist(),
                index=sdk_data["qubits"]
            ).fillna(0)

            equiv_df.plot(
                kind="bar",
                stacked=True,
                ax=ax,
                legend=False,
                color=[EQUIV_COLOR_MAP[c] for c in equiv_df.columns],
            )

            handles, labels = ax.get_legend_handles_labels()

            for h, l in zip(handles, labels):
                legend_items[l] = h

            ax.set_title(sdk_name.split('_')[0])
            ax.set_xlabel("Qubits")
            ax.set_ylabel("Runs")


        fig.legend(
            legend_items.values(),
            legend_items.keys(),
            title="Equivalence",
            loc="lower center",
            ncol=len(legend_items)
        )

        plt.savefig(f"{path}/{algo}_{folder}.png")
        plt.close()
        #plt.show()
