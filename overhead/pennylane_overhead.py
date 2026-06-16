import time
import pennylane as qp


qc = qp.tape.QuantumScript()
start_time = time.time()
qp.compile(qc)
end_time = time.time()
duration_ms_1 = (end_time - start_time) * 1000


start_time = time.time()
qp.compile(qc)
end_time = time.time()
duration_ms_2 = (end_time - start_time) * 1000
print(f"{duration_ms_1};{duration_ms_2}")