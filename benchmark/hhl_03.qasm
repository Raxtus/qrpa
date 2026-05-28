// Benchmark created by MQT Bench on 2026-05-28
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm3

OPENQASM 3.0;
include "stdgates.inc";
gate qft_dg _gate_q_0 {
  h _gate_q_0;
}
gate qft _gate_q_0 {
  h _gate_q_0;
}
bit[1] c;
qubit[1] sys;
qubit[1] phase_0;
qubit[1] ancilla;
x sys[0];
h phase_0[0];
cp(11.366282220687872) phase_0[0], sys[0];
qft_dg phase_0[0];
cry(1.1714210053478946) phase_0[0], ancilla[0];
qft phase_0[0];
cp(-11.366282220687872) phase_0[0], sys[0];
h phase_0[0];
c[0] = measure sys[0];
