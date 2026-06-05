// Benchmark created by MQT Bench on 2026-06-05
// For more info: https://mqt-bench.app/
// MQT Bench version: 2.2.2
// Qiskit version: 2.4.1
// Output format: qasm3

OPENQASM 3.0;
include "stdgates.inc";
gate ccz _gate_q_0, _gate_q_1, _gate_q_2 {
  h _gate_q_2;
  ccx _gate_q_0, _gate_q_1, _gate_q_2;
  h _gate_q_2;
}
gate rccx _gate_q_0, _gate_q_1, _gate_q_2 {
  h _gate_q_2;
  t _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  tdg _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  t _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  tdg _gate_q_2;
  h _gate_q_2;
}
gate rzx(p0) _gate_q_0, _gate_q_1 {
  h _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  h _gate_q_1;
}
gate rcccx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3 {
  h _gate_q_3;
  t _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  tdg _gate_q_3;
  h _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  t _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  tdg _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  t _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  tdg _gate_q_3;
  h _gate_q_3;
  t _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  tdg _gate_q_3;
  h _gate_q_3;
}
gate ecr _gate_q_0, _gate_q_1 {
  s _gate_q_0;
  sx _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  x _gate_q_0;
}
gate c3sx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3 {
  h _gate_q_3;
  cp(pi/8) _gate_q_0, _gate_q_3;
  h _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  h _gate_q_3;
  cp(-pi/8) _gate_q_1, _gate_q_3;
  h _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  h _gate_q_3;
  cp(pi/8) _gate_q_1, _gate_q_3;
  h _gate_q_3;
  cx _gate_q_1, _gate_q_2;
  h _gate_q_3;
  cp(-pi/8) _gate_q_2, _gate_q_3;
  h _gate_q_3;
  cx _gate_q_0, _gate_q_2;
  h _gate_q_3;
  cp(pi/8) _gate_q_2, _gate_q_3;
  h _gate_q_3;
  cx _gate_q_1, _gate_q_2;
  h _gate_q_3;
  cp(-pi/8) _gate_q_2, _gate_q_3;
  h _gate_q_3;
  cx _gate_q_0, _gate_q_2;
  h _gate_q_3;
  cp(pi/8) _gate_q_2, _gate_q_3;
  h _gate_q_3;
}
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}
gate cu1(p0) _gate_q_0, _gate_q_1 {
  p(0.5*p0) _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  p((-0.5)*p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  p(0.5*p0) _gate_q_1;
}
gate cs _gate_q_0, _gate_q_1 {
  t _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  tdg _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  t _gate_q_1;
}
gate dcx _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_0;
}
gate r(p0, p1) _gate_q_0 {
  U(p0, -pi/2 + p1, pi/2 - p1) _gate_q_0;
}
gate cu3(p0, p1, p2) _gate_q_0, _gate_q_1 {
  p(0.5*p2 + 0.5*p1) _gate_q_0;
  p(0.5*p2 - 0.5*p1) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  U((-0.5)*p0, 0, (-0.5)*p1 - 0.5*p2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  U(0.5*p0, p1, 0) _gate_q_1;
}
bit[11] meas;
qubit[11] q;
cswap q[10], q[6], q[8];
t q[5];
ccz q[7], q[1], q[4];
rccx q[0], q[3], q[9];
rzx(3.772222268266399) q[8], q[7];
rcccx q[2], q[0], q[3], q[4];
cswap q[5], q[10], q[9];
ecr q[6], q[1];
rccx q[3], q[5], q[4];
swap q[2], q[1];
tdg q[0];
ccx q[6], q[7], q[10];
u3(5.076820509783505, 5.29650934899458, 4.999421715326975) q[9];
rccx q[9], q[10], q[8];
c3sx q[2], q[0], q[6], q[7];
ccx q[5], q[3], q[4];
sx q[1];
u1(4.973898923189498) q[8];
rzz(0.27841736785903115) q[6], q[1];
ccz q[3], q[0], q[7];
h q[10];
ccz q[5], q[9], q[4];
ccx q[2], q[4], q[8];
c3sx q[6], q[7], q[5], q[1];
ch q[9], q[0];
ccx q[8], q[0], q[5];
ccz q[7], q[9], q[2];
rcccx q[4], q[10], q[1], q[3];
h q[6];
rccx q[9], q[4], q[7];
rcccx q[1], q[3], q[10], q[8];
cswap q[2], q[0], q[5];
u2(3.62694954519184, 2.4253360614089803) q[3];
z q[5];
c3sx q[1], q[2], q[4], q[6];
sdg q[7];
ccx q[9], q[10], q[0];
sdg q[8];
cswap q[2], q[10], q[1];
rccx q[4], q[9], q[7];
rx(3.464488948976134) q[0];
s q[3];
cswap q[8], q[6], q[5];
s q[8];
tdg q[2];
ccx q[10], q[7], q[0];
rcccx q[4], q[1], q[3], q[5];
cu1(4.456422858305494) q[9], q[6];
t q[5];
cx q[6], q[3];
cs q[2], q[9];
cswap q[0], q[4], q[8];
u1(3.3494623773395826) q[7];
cswap q[8], q[7], q[5];
cu(0.5967658627927318, 4.681014540698367, 4.710976327241525, 1.5323338718178692) q[0], q[4];
x q[9];
cs q[10], q[2];
rccx q[1], q[6], q[3];
cswap q[7], q[6], q[9];
ccz q[0], q[2], q[10];
rx(4.703173468806573) q[5];
dcx q[8], q[1];
ccz q[2], q[0], q[4];
cswap q[1], q[10], q[9];
cy q[3], q[8];
r(2.836148587154802, 2.833584415720613) q[5];
t q[7];
rccx q[5], q[2], q[10];
id q[1];
c3sx q[0], q[7], q[3], q[6];
ccz q[4], q[9], q[8];
cswap q[2], q[8], q[6];
cswap q[5], q[0], q[4];
cu3(2.296369071021966, 0.21420527290543262, 4.956735330393394) q[7], q[1];
cswap q[3], q[9], q[10];
ccz q[8], q[5], q[0];
rz(0.27333525938642017) q[2];
cswap q[4], q[6], q[3];
ccx q[1], q[9], q[10];
rcccx q[7], q[5], q[3], q[6];
swap q[9], q[0];
ccz q[1], q[10], q[2];
rcccx q[9], q[3], q[4], q[2];
ch q[10], q[0];
c3sx q[5], q[6], q[8], q[7];
ccz q[4], q[9], q[0];
ccx q[8], q[6], q[3];
ccz q[10], q[7], q[2];
cu1(2.3749623468387755) q[5], q[1];
rccx q[3], q[1], q[10];
sx q[2];
cry(5.080419195668465) q[5], q[6];
cswap q[7], q[4], q[9];
id q[8];
barrier q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
meas[5] = measure q[5];
meas[6] = measure q[6];
meas[7] = measure q[7];
meas[8] = measure q[8];
meas[9] = measure q[9];
meas[10] = measure q[10];
