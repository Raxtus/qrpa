import time
import logging
import matplotlib.pyplot as plt
import numpy as np

from bqskit.compiler import Compiler
from bqskit.ir import Circuit
from bqskit.passes import NOOPPass

#logging.basicConfig(level=logging.DEBUG)

# Number of repetitions for each measurement
x = 10

# Lists to store results
server_times = []
compilation_times = []

# Measure server start and close times
for i in range(x):
    start_time = time.perf_counter()
    compiler = Compiler(num_workers=1)
    compiler.close()
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000
    server_times.append(duration_ms)

# Measure start and close with dummy compilation
qc = Circuit(num_qudits=2)
workflow = [NOOPPass()]

for i in range(x):
    start_time = time.perf_counter()
    compiler = Compiler(num_workers=1)
    compiler.compile(circuit=qc, workflow=workflow)
    compiler.close()
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000
    compilation_times.append(duration_ms)

# Display aggregate results
print(f"Server start and close ({x} repetitions):")
print(f"Average time: {sum(server_times)/x:.3f} ms")
print(f"Shortest time: {min(server_times):.3f} ms")
print(f"Longest time: {max(server_times):.3f} ms\n")

print(f"Start and close with dummy compilation ({x} repetitions):")
print(f"Average time: {sum(compilation_times)/x:.3f} ms")
print(f"Shortest time: {min(compilation_times):.3f} ms")
print(f"Longest time: {max(compilation_times):.3f} ms\n")

avg_server_time = np.mean(server_times)
avg_compilation_time = np.mean(compilation_times)

fig, ax1 = plt.subplots(figsize=(6, 8))
ax2 = ax1.twinx()

# Server times on left y-axis
ax1.scatter(1, server_times, color='blue', label='Server start/close', alpha=0.6)
ax1.scatter(1, avg_server_time, color='red', s=200, label='Server avg', marker='s')
ax1.set_ylabel('Server Time (ms)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Compilation times on right y-axis
ax2.scatter(2, compilation_times, color='green', label='Dummy compilation', alpha=0.6)
ax2.scatter(2, avg_compilation_time, color='orange', s=200, label='Compilation avg', marker='s')
ax2.set_ylabel('Compilation Time (ms)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# X-axis
ax1.set_xticks([1, 2], ['Server', 'Compilation'])
ax1.set_xlim(0.5, 2.5)

# Grid
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Combined legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='best')

plt.title('Measurement Results with Averages')
plt.tight_layout()
plt.show()