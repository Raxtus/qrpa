// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm3

OPENQASM 3.0;
include "stdgates.inc";
bit[2] meas;
qubit[2] q;
ry(6.006735895579343) q[0];
ry(1.304903297657757) q[1];
cx q[0], q[1];
ry(5.205272730965009) q[0];
ry(0.9379672423735244) q[1];
cx q[0], q[1];
ry(3.2220464314480877) q[0];
ry(0.8540080589393146) q[1];
cx q[0], q[1];
ry(4.329343885871547) q[0];
ry(5.288856933750764) q[1];
barrier q[0], q[1];
meas[0] = measure q[0];
meas[1] = measure q[1];
