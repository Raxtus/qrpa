// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm2

OPENQASM 2.0;
include "qelib1.inc";
gate qft_dg q0,q1,q2 { swap q0,q2; h q0; cp(-pi/2) q1,q0; h q1; cp(-pi/4) q2,q0; cp(-pi/2) q2,q1; h q2; }
gate qft q0,q1,q2 { h q2; cp(pi/2) q2,q1; cp(pi/4) q2,q0; h q1; cp(pi/2) q1,q0; h q0; swap q0,q2; }
qreg sys[1];
qreg phase[3];
qreg ancilla[1];
creg c[1];
x sys[0];
h phase[0];
h phase[1];
h phase[2];
cp(11.366282220687872) phase[0],sys[0];
cp(5.683141110343936) phase[1],sys[0];
cp(2.841570555171968) phase[2],sys[0];
qft_dg phase[0],phase[1],phase[2];
cry(pi) phase[0],ancilla[0];
cry(pi) phase[1],ancilla[0];
cry(1.1714210053478946) phase[2],ancilla[0];
qft phase[0],phase[1],phase[2];
cp(-2.841570555171968) phase[2],sys[0];
cp(-5.683141110343936) phase[1],sys[0];
cp(-11.366282220687872) phase[0],sys[0];
h phase[0];
h phase[1];
h phase[2];
measure sys[0] -> c[0];
