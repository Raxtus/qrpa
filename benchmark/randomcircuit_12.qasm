// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm2

OPENQASM 2.0;
include "qelib1.inc";
gate ccz q0,q1,q2 { h q2; ccx q0,q1,q2; h q2; }
gate cs q0,q1 { t q0; cx q0,q1; tdg q1; cx q0,q1; t q1; }
gate rcccx q0,q1,q2,q3 { h q3; t q3; cx q2,q3; tdg q3; h q3; cx q0,q3; t q3; cx q1,q3; tdg q3; cx q0,q3; t q3; cx q1,q3; tdg q3; h q3; t q3; cx q2,q3; tdg q3; h q3; }
gate ecr q0,q1 { s q0; sx q1; cx q0,q1; x q0; }
gate xx_plus_yy(param0,param1) q0,q1 { rz(param1) q0; sdg q1; sx q1; s q1; s q0; cx q1,q0; ry((-0.5)*param0) q1; ry((-0.5)*param0) q0; cx q1,q0; sdg q0; sdg q1; sxdg q1; s q1; rz(-param1) q0; }
gate r(param0,param1) q0 { u(param0,-pi/2 + param1,pi/2 - param1) q0; }
gate dcx q0,q1 { cx q0,q1; cx q1,q0; }
gate ryy(param0) q0,q1 { sxdg q0; sxdg q1; cx q0,q1; rz(param0) q1; cx q0,q1; sx q0; sx q1; }
qreg q[12];
creg meas[12];
cswap q[3],q[7],q[2];
t q[5];
ccz q[10],q[8],q[9];
rccx q[11],q[6],q[1];
cs q[4],q[0];
rcccx q[8],q[2],q[4],q[1];
cswap q[10],q[3],q[7];
ecr q[6],q[11];
cz q[9],q[5];
sdg q[0];
tdg q[10];
ccx q[0],q[7],q[4];
ccx q[8],q[3],q[1];
cswap q[9],q[5],q[2];
p(4.999421715326975) q[6];
rccx q[8],q[11],q[1];
c3sqrtx q[3],q[7],q[4],q[2];
ccx q[5],q[6],q[9];
ccz q[1],q[2],q[0];
h q[10];
ccz q[5],q[4],q[11];
cy q[6],q[8];
u3(1.5699311213649152,2.6845301397458154,4.966942791122286) q[7];
ccx q[5],q[3],q[11];
tdg q[8];
rccx q[10],q[6],q[4];
ccx q[0],q[9],q[1];
rcccx q[1],q[9],q[4],q[8];
ccx q[2],q[3],q[10];
ccx q[11],q[0],q[7];
c3sqrtx q[1],q[9],q[2],q[11];
rccx q[0],q[5],q[8];
cswap q[6],q[3],q[10];
crx(1.2956580914789548) q[7],q[4];
t q[8];
rccx q[3],q[0],q[4];
cswap q[1],q[7],q[2];
ccx q[11],q[9],q[10];
u1(6.120485443197035) q[5];
xx_plus_yy(2.2523109408064848,0.6752251705099757) q[9],q[8];
ccz q[3],q[7],q[6];
crz(2.20615164388034) q[4],q[0];
ccz q[11],q[10],q[1];
r(1.3265260797643066,5.072059083852748) q[5];
t q[6];
cx q[5],q[7];
cs q[2],q[1];
cswap q[8],q[0],q[3];
u1(0.6588322068820782) q[10];
ccz q[11],q[4],q[9];
cs q[10],q[0];
rcccx q[11],q[6],q[8],q[3];
ccx q[1],q[9],q[2];
ccx q[4],q[5],q[7];
ccz q[6],q[4],q[0];
rx(2.5357857195377083) q[8];
dcx q[2],q[7];
ccz q[3],q[9],q[11];
rccx q[1],q[5],q[10];
cswap q[0],q[8],q[1];
cy q[3],q[10];
r(3.4047365073538574,6.238651213351592) q[7];
t q[4];
rcccx q[9],q[2],q[6],q[5];
ccz q[0],q[3],q[1];
ccz q[11],q[10],q[5];
ccz q[8],q[4],q[9];
cswap q[2],q[7],q[6];
cswap q[5],q[8],q[9];
rccx q[11],q[2],q[7];
ccz q[1],q[3],q[0];
cswap q[6],q[10],q[4];
ccx q[10],q[11],q[1];
c3sqrtx q[0],q[7],q[4],q[8];
cswap q[5],q[2],q[6];
crz(6.146016660618906) q[3],q[9];
ccx q[2],q[6],q[1];
ccz q[8],q[11],q[5];
rccx q[0],q[4],q[7];
sx q[3];
y q[10];
y q[9];
u(0.6647375436450751,3.568967231508171,5.468967898137674) q[0];
ccz q[10],q[2],q[6];
ccx q[9],q[3],q[4];
ccz q[1],q[8],q[7];
cz q[5],q[11];
sx q[4];
rccx q[2],q[3],q[1];
sx q[11];
cry(5.080419195668465) q[5],q[9];
cswap q[8],q[0],q[10];
id q[6];
rccx q[5],q[3],q[11];
cz q[10],q[4];
cswap q[7],q[8],q[0];
ryy(0.493448912319289) q[1],q[2];
y q[9];
cz q[0],q[6];
ccx q[11],q[3],q[10];
h q[2];
c3sqrtx q[8],q[7],q[5],q[1];
rcccx q[7],q[0],q[5],q[11];
rccx q[3],q[9],q[6];
ccz q[1],q[10],q[2];
rcccx q[6],q[8],q[5],q[10];
h q[3];
rccx q[7],q[9],q[4];
ccz q[11],q[0],q[2];
barrier q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9],q[10],q[11];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
measure q[4] -> meas[4];
measure q[5] -> meas[5];
measure q[6] -> meas[6];
measure q[7] -> meas[7];
measure q[8] -> meas[8];
measure q[9] -> meas[9];
measure q[10] -> meas[10];
measure q[11] -> meas[11];
