// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm2

OPENQASM 2.0;
include "qelib1.inc";
gate ccz q0,q1,q2 { h q2; ccx q0,q1,q2; h q2; }
gate rzx(param0) q0,q1 { h q1; cx q0,q1; rz(param0) q1; cx q0,q1; h q1; }
gate rcccx q0,q1,q2,q3 { h q3; t q3; cx q2,q3; tdg q3; h q3; cx q0,q3; t q3; cx q1,q3; tdg q3; cx q0,q3; t q3; cx q1,q3; tdg q3; h q3; t q3; cx q2,q3; tdg q3; h q3; }
gate ecr q0,q1 { s q0; sx q1; cx q0,q1; x q0; }
gate cs q0,q1 { t q0; cx q0,q1; tdg q1; cx q0,q1; t q1; }
gate dcx q0,q1 { cx q0,q1; cx q1,q0; }
gate r(param0,param1) q0 { u(param0,-pi/2 + param1,pi/2 - param1) q0; }
qreg q[11];
creg meas[11];
cswap q[10],q[6],q[8];
t q[5];
ccz q[7],q[1],q[4];
rccx q[0],q[3],q[9];
rzx(3.772222268266399) q[8],q[7];
rcccx q[2],q[0],q[3],q[4];
cswap q[5],q[10],q[9];
ecr q[6],q[1];
rccx q[3],q[5],q[4];
swap q[2],q[1];
tdg q[0];
ccx q[6],q[7],q[10];
u3(5.076820509783505,5.29650934899458,4.999421715326975) q[9];
rccx q[9],q[10],q[8];
c3sqrtx q[2],q[0],q[6],q[7];
ccx q[5],q[3],q[4];
sx q[1];
u1(4.973898923189498) q[8];
rzz(0.27841736785903115) q[6],q[1];
ccz q[3],q[0],q[7];
h q[10];
ccz q[5],q[9],q[4];
ccx q[2],q[4],q[8];
c3sqrtx q[6],q[7],q[5],q[1];
ch q[9],q[0];
ccx q[8],q[0],q[5];
ccz q[7],q[9],q[2];
rcccx q[4],q[10],q[1],q[3];
h q[6];
rccx q[9],q[4],q[7];
rcccx q[1],q[3],q[10],q[8];
cswap q[2],q[0],q[5];
u2(3.62694954519184,2.4253360614089803) q[3];
z q[5];
c3sqrtx q[1],q[2],q[4],q[6];
sdg q[7];
ccx q[9],q[10],q[0];
sdg q[8];
cswap q[2],q[10],q[1];
rccx q[4],q[9],q[7];
rx(3.464488948976134) q[0];
s q[3];
cswap q[8],q[6],q[5];
s q[8];
tdg q[2];
ccx q[10],q[7],q[0];
rcccx q[4],q[1],q[3],q[5];
cu1(4.456422858305494) q[9],q[6];
t q[5];
cx q[6],q[3];
cs q[2],q[9];
cswap q[0],q[4],q[8];
u1(3.3494623773395826) q[7];
cswap q[8],q[7],q[5];
cu(0.5967658627927318,4.681014540698367,4.710976327241525,1.5323338718178692) q[0],q[4];
x q[9];
cs q[10],q[2];
rccx q[1],q[6],q[3];
cswap q[7],q[6],q[9];
ccz q[0],q[2],q[10];
rx(4.703173468806573) q[5];
dcx q[8],q[1];
ccz q[2],q[0],q[4];
cswap q[1],q[10],q[9];
cy q[3],q[8];
r(2.836148587154802,2.833584415720613) q[5];
t q[7];
rccx q[5],q[2],q[10];
id q[1];
c3sqrtx q[0],q[7],q[3],q[6];
ccz q[4],q[9],q[8];
cswap q[2],q[8],q[6];
cswap q[5],q[0],q[4];
cu3(2.296369071021966,0.21420527290543262,4.956735330393394) q[7],q[1];
cswap q[3],q[9],q[10];
ccz q[8],q[5],q[0];
rz(0.27333525938642017) q[2];
cswap q[4],q[6],q[3];
ccx q[1],q[9],q[10];
rcccx q[7],q[5],q[3],q[6];
swap q[9],q[0];
ccz q[1],q[10],q[2];
rcccx q[9],q[3],q[4],q[2];
ch q[10],q[0];
c3sqrtx q[5],q[6],q[8],q[7];
ccz q[4],q[9],q[0];
ccx q[8],q[6],q[3];
ccz q[10],q[7],q[2];
cu1(2.3749623468387755) q[5],q[1];
rccx q[3],q[1],q[10];
sx q[2];
cry(5.080419195668465) q[5],q[6];
cswap q[7],q[4],q[9];
id q[8];
barrier q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9],q[10];
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
