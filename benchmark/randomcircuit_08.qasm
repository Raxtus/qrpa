// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm2

OPENQASM 2.0;
include "qelib1.inc";
gate ccz q0,q1,q2 { h q2; ccx q0,q1,q2; h q2; }
gate dcx q0,q1 { cx q0,q1; cx q1,q0; }
gate ryy(param0) q0,q1 { sxdg q0; sxdg q1; cx q0,q1; rz(param0) q1; cx q0,q1; sx q0; sx q1; }
gate rcccx q0,q1,q2,q3 { h q3; t q3; cx q2,q3; tdg q3; h q3; cx q0,q3; t q3; cx q1,q3; tdg q3; cx q0,q3; t q3; cx q1,q3; tdg q3; h q3; t q3; cx q2,q3; tdg q3; h q3; }
qreg q[8];
creg meas[8];
cswap q[6],q[7],q[5];
t q[1];
ccz q[2],q[0],q[3];
t q[2];
c3sqrtx q[0],q[7],q[6],q[1];
dcx q[5],q[4];
cu(2.1332392738715247,0.9334849134188741,2.871537495561712,2.7511828987678966) q[4],q[5];
tdg q[0];
t q[2];
cry(3.607915524002728) q[1],q[6];
ch q[3],q[5];
rccx q[1],q[7],q[0];
cswap q[4],q[6],q[2];
rccx q[5],q[3],q[0];
c3sqrtx q[7],q[6],q[4],q[1];
ccz q[5],q[4],q[3];
cswap q[2],q[1],q[7];
u3(1.5699311213649152,2.6845301397458154,4.966942791122286) q[3];
cswap q[2],q[7],q[0];
ccx q[4],q[6],q[5];
ry(3.3401519228349494) q[1];
ch q[1],q[7];
ccx q[5],q[2],q[0];
tdg q[6];
cp(2.510079506040741) q[2],q[1];
cswap q[4],q[5],q[6];
ccx q[0],q[3],q[7];
ccx q[2],q[5],q[0];
ccz q[3],q[1],q[7];
cy q[1],q[3];
c3sqrtx q[4],q[7],q[2],q[5];
rccx q[2],q[6],q[3];
u2(0.12608146472089976,5.306484114352285) q[0];
z q[5];
ccx q[4],q[7],q[1];
cswap q[3],q[2],q[5];
ccx q[1],q[0],q[4];
ryy(0.6403822025770108) q[7],q[6];
cswap q[0],q[1],q[4];
ccx q[2],q[7],q[5];
cx q[6],q[3];
rcccx q[6],q[5],q[3],q[0];
cswap q[7],q[4],q[1];
sxdg q[2];
rcccx q[5],q[6],q[4],q[3];
rccx q[1],q[0],q[7];
barrier q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
measure q[4] -> meas[4];
measure q[5] -> meas[5];
measure q[6] -> meas[6];
measure q[7] -> meas[7];
