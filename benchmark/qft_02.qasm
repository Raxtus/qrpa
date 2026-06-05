// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm3

OPENQASM 3.0;
include "stdgates.inc";
gate qft _gate_q_0, _gate_q_1 {
  h _gate_q_1;
  cp(pi/2) _gate_q_1, _gate_q_0;
  h _gate_q_0;
  swap _gate_q_0, _gate_q_1;
}
bit[2] meas;
qubit[2] q;
qft q[0], q[1];
barrier q[0], q[1];
meas[0] = measure q[0];
meas[1] = measure q[1];
