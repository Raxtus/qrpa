// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm2

OPENQASM 2.0;
include "qelib1.inc";
gate ccz q0,q1,q2 { h q2; ccx q0,q1,q2; h q2; }
gate dcx q0,q1 { cx q0,q1; cx q1,q0; }
gate rcccx q0,q1,q2,q3 { h q3; t q3; cx q2,q3; tdg q3; h q3; cx q0,q3; t q3; cx q1,q3; tdg q3; cx q0,q3; t q3; cx q1,q3; tdg q3; h q3; t q3; cx q2,q3; tdg q3; h q3; }
gate xx_plus_yy(param0,param1) q0,q1 { rz(param1) q0; sdg q1; sx q1; s q1; s q0; cx q1,q0; ry((-0.5)*param0) q1; ry((-0.5)*param0) q0; cx q1,q0; sdg q0; sdg q1; sxdg q1; s q1; rz(-param1) q0; }
gate ryy(param0) q0,q1 { sxdg q0; sxdg q1; cx q0,q1; rz(param0) q1; cx q0,q1; sx q0; sx q1; }
gate iswap q0,q1 { s q0; s q1; h q0; cx q0,q1; cx q1,q0; h q1; }
qreg q[9];
creg meas[9];
cswap q[5],q[7],q[4];
t q[0];
ccz q[3],q[1],q[2];
swap q[6],q[8];
t q[3];
c3sqrtx q[6],q[7],q[5],q[0];
dcx q[1],q[4];
cu(0.9334849134188741,2.871537495561712,2.7511828987678966,3.607915524002728) q[4],q[7];
tdg q[3];
t q[6];
cry(2.3453197008450233) q[5],q[8];
ccx q[2],q[1],q[0];
rccx q[2],q[6],q[8];
rccx q[0],q[5],q[7];
rccx q[3],q[1],q[4];
rccx q[8],q[4],q[5];
swap q[0],q[7];
cswap q[3],q[1],q[6];
u1(0.6044551176832745) q[6];
rzz(4.458303280933144) q[2],q[3];
ccz q[8],q[1],q[4];
h q[0];
sx q[1];
sx q[3];
ccx q[4],q[2],q[0];
c3sqrtx q[6],q[5],q[8],q[7];
cp(2.342819928892192) q[4],q[2];
cswap q[6],q[7],q[1];
rcccx q[3],q[8],q[0],q[5];
ccz q[6],q[7],q[1];
ccz q[4],q[3],q[8];
ccx q[5],q[0],q[2];
cswap q[0],q[3],q[2];
rccx q[7],q[8],q[6];
ccx q[1],q[4],q[5];
ccx q[7],q[8],q[1];
sdg q[3];
ccz q[4],q[2],q[0];
sx q[6];
ccx q[0],q[5],q[4];
cswap q[6],q[7],q[2];
rccx q[1],q[3],q[8];
xx_plus_yy(5.935241355219743,3.650842432466433) q[1],q[0];
ccz q[2],q[6],q[5];
crz(0.7871534634082653) q[7],q[4];
z q[0];
rccx q[8],q[1],q[6];
ccz q[4],q[2],q[5];
ryy(3.0509600791917504) q[7],q[3];
c3sqrtx q[5],q[3],q[2],q[6];
u1(0.9377220734486331) q[4];
rccx q[0],q[1],q[8];
u3(4.36209501550468,0.8826812454603556,5.995865513716156) q[7];
rcccx q[8],q[6],q[0],q[4];
ccx q[2],q[7],q[5];
iswap q[6],q[3];
t q[7];
c3sqrtx q[4],q[1],q[8],q[0];
ccz q[3],q[2],q[1];
rcccx q[4],q[0],q[8],q[7];
barrier q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
measure q[4] -> meas[4];
measure q[5] -> meas[5];
measure q[6] -> meas[6];
measure q[7] -> meas[7];
measure q[8] -> meas[8];
