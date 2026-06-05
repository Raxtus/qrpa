// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm2

OPENQASM 2.0;
include "qelib1.inc";
gate qft_dg q0,q1 { swap q0,q1; h q0; cp(-pi/2) q1,q0; h q1; }
gate qft q0,q1 { h q1; cp(pi/2) q1,q0; h q0; swap q0,q1; }
qreg sys[1];
qreg phase[2];
qreg ancilla[1];
creg c[1];
x sys[0];
h phase[0];
h phase[1];
cp(11.366282220687872) phase[0],sys[0];
cp(5.683141110343936) phase[1],sys[0];
qft_dg phase[0],phase[1];
cry(pi) phase[0],ancilla[0];
cry(1.1714210053478946) phase[1],ancilla[0];
qft phase[0],phase[1];
cp(-5.683141110343936) phase[1],sys[0];
cp(-11.366282220687872) phase[0],sys[0];
h phase[0];
h phase[1];
measure sys[0] -> c[0];
