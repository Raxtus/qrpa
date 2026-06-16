import time
import qiskit
from qiskit import QuantumCircuit

qc = QuantumCircuit()
start_time = time.time()
qiskit.transpile(qc)
end_time = time.time()
duration_ms = (end_time - start_time) * 1000

print(duration_ms)

start_time = time.time()
qiskit.transpile(qc)
end_time = time.time()
duration_ms = (end_time - start_time) * 1000
print(duration_ms)