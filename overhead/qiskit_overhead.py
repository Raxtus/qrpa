import time
import qiskit
from Cython.Shadow import returns
from qiskit import QuantumCircuit

qc = QuantumCircuit()
start_time = time.time()
qiskit.transpile(qc)
end_time = time.time()
duration_ms_1 = (end_time - start_time) * 1000


start_time = time.time()
qiskit.transpile(qc)
end_time = time.time()
duration_ms_2 = (end_time - start_time) * 1000
print(f"{duration_ms_1};{duration_ms_2}")