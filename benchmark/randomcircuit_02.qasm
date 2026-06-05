// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm2

OPENQASM 2.0;
include "qelib1.inc";
gate csdg q0,q1 { tdg q0; cx q0,q1; t q1; cx q0,q1; tdg q1; }
qreg q[2];
creg meas[2];
rxx(3.2220464314480877) q[0],q[1];
crx(2.6735518805676657) q[1],q[0];
csdg q[0],q[1];
y q[1];
p(5.196847304624584) q[0];
barrier q[0],q[1];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
