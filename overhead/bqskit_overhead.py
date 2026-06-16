import time
import logging
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

