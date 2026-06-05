// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm2

OPENQASM 2.0;
include "qelib1.inc";
gate qft q0,q1 { h q1; cp(pi/2) q1,q0; h q0; swap q0,q1; }
qreg q[2];
creg meas[2];
qft q[0],q[1];
barrier q[0],q[1];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
