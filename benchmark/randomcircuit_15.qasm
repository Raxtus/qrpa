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
gate cu1(p0) _gate_q_0, _gate_q_1 {
  p(0.5*p0) _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  p((-0.5)*p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  p(0.5*p0) _gate_q_1;
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
gate r(p0, p1) _gate_q_0 {
  U(p0, -pi/2 + p1, pi/2 - p1) _gate_q_0;
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
gate sxdg _gate_q_0 {
  s _gate_q_0;
  h _gate_q_0;
  s _gate_q_0;
}
gate ryy(p0) _gate_q_0, _gate_q_1 {
  sxdg _gate_q_0;
  sxdg _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  sx _gate_q_0;
  sx _gate_q_1;
}
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}
gate xx_plus_yy(p0, p1) _gate_q_0, _gate_q_1 {
  rz(p1) _gate_q_0;
  sdg _gate_q_1;
  sx _gate_q_1;
  s _gate_q_1;
  s _gate_q_0;
  cx _gate_q_1, _gate_q_0;
  ry((-0.5)*p0) _gate_q_1;
  ry((-0.5)*p0) _gate_q_0;
  cx _gate_q_1, _gate_q_0;
  sdg _gate_q_0;
  sdg _gate_q_1;
  sxdg _gate_q_1;
  s _gate_q_1;
  rz(-p1) _gate_q_0;
}
gate iswap _gate_q_0, _gate_q_1 {
  s _gate_q_0;
  s _gate_q_1;
  h _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_0;
  h _gate_q_1;
}
gate dcx _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_0;
}
gate xx_minus_yy(p0, p1) _gate_q_0, _gate_q_1 {
  rz(-p1) _gate_q_1;
  sdg _gate_q_0;
  sx _gate_q_0;
  s _gate_q_0;
  s _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  ry(0.5*p0) _gate_q_0;
  ry((-0.5)*p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  sdg _gate_q_1;
  sdg _gate_q_0;
  sxdg _gate_q_0;
  s _gate_q_0;
  rz(p1) _gate_q_1;
}
gate rzx(p0) _gate_q_0, _gate_q_1 {
  h _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  h _gate_q_1;
}
gate csdg _gate_q_0, _gate_q_1 {
  tdg _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  t _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  tdg _gate_q_1;
}
bit[15] meas;
qubit[15] q;
cswap q[7], q[12], q[1];
t q[14];
ccz q[11], q[9], q[10];
rccx q[8], q[13], q[2];
ccx q[3], q[6], q[5];
cu1(1.4207188874050238) q[4], q[0];
cu(0.7203317518888239, 1.4645506429344954, 4.820717485323253, 6.202284721500185) q[11], q[10];
tdg q[9];
t q[1];
cry(5.076820509783505) q[5], q[14];
ccx q[6], q[2], q[12];
ccz q[4], q[13], q[0];
rccx q[7], q[8], q[3];
rccx q[11], q[14], q[3];
c3sx q[2], q[6], q[4], q[12];
ccx q[9], q[5], q[0];
rccx q[7], q[8], q[13];
swap q[1], q[10];
u3(5.625348551233995, 1.454894982862097, 2.791946771572743) q[1];
cswap q[14], q[7], q[5];
ccx q[3], q[0], q[6];
ry(0.9052373921267518) q[4];
ccz q[10], q[12], q[11];
rccx q[2], q[8], q[9];
r(5.087406807216837, 2.401193884234052) q[13];
rcccx q[8], q[10], q[13], q[5];
cz q[11], q[14];
ccx q[3], q[7], q[4];
ccz q[9], q[0], q[1];
sdg q[12];
c3sx q[14], q[7], q[11], q[10];
rccx q[4], q[3], q[0];
cswap q[9], q[8], q[1];
rccx q[6], q[5], q[2];
u2(2.3386467136971576, 0.7377781957483639) q[13];
ccx q[1], q[4], q[2];
ryy(3.464488948976134) q[0], q[10];
rcccx q[6], q[11], q[5], q[8];
ccx q[13], q[9], q[14];
cswap q[12], q[3], q[7];
cswap q[4], q[1], q[14];
sxdg q[9];
cswap q[8], q[0], q[10];
ccx q[7], q[13], q[11];
s q[3];
ccx q[6], q[5], q[2];
z q[12];
u1(5.936603552194878) q[2];
rccx q[11], q[3], q[8];
u3(2.4951327774590375, 5.590233885125366, 0.45529085355760135) q[13];
cswap q[0], q[6], q[5];
U(1.6643787200110323, 5.848967225057895, 2.312266393217539) q[12];
cswap q[4], q[7], q[10];
s q[14];
rzz(0.5967658627927318) q[9], q[1];
c3sx q[11], q[12], q[13], q[8];
cswap q[14], q[4], q[10];
cswap q[1], q[9], q[0];
ccz q[5], q[3], q[6];
rx(2.5357857195377083) q[7];
r(4.6953643466626085, 5.298397105888836) q[4];
t q[8];
rcccx q[14], q[13], q[3], q[10];
ccx q[11], q[2], q[0];
u1(0.040797012819164896) q[5];
rx(5.829162861548355) q[9];
rccx q[7], q[6], q[1];
tdg q[12];
ccz q[9], q[2], q[1];
xx_plus_yy(2.666608411818102, 1.1830689753069417) q[4], q[3];
ccx q[5], q[8], q[14];
rccx q[12], q[13], q[7];
ccz q[11], q[6], q[10];
ccz q[8], q[5], q[13];
rz(5.968666496003319) q[9];
cswap q[4], q[2], q[11];
ccx q[12], q[14], q[6];
rccx q[1], q[10], q[3];
iswap q[0], q[7];
dcx q[6], q[1];
rccx q[13], q[12], q[5];
c3sx q[14], q[11], q[9], q[2];
ccx q[4], q[0], q[8];
ccz q[7], q[3], q[10];
U(5.6946507737984255, 0.6246238923704159, 2.3749623468387755) q[1];
ccz q[2], q[12], q[9];
ccx q[5], q[8], q[6];
ccz q[14], q[0], q[13];
cz q[11], q[3];
t q[10];
xx_minus_yy(4.7046749871144575, 3.007679600008536) q[4], q[7];
ccx q[0], q[6], q[5];
cswap q[11], q[4], q[3];
p(3.2640054194738153) q[9];
rccx q[14], q[2], q[1];
rccx q[13], q[7], q[12];
crx(1.8617254523671918) q[10], q[8];
rx(1.3516280770480866) q[4];
cy q[6], q[5];
rx(2.080600083403383) q[11];
c3sx q[14], q[0], q[13], q[1];
rcccx q[2], q[10], q[8], q[7];
cswap q[12], q[9], q[3];
rccx q[8], q[6], q[2];
rx(2.318350220204926) q[11];
ccx q[14], q[4], q[12];
rcccx q[10], q[5], q[3], q[0];
rccx q[13], q[7], q[1];
rcccx q[14], q[12], q[6], q[4];
h q[2];
rccx q[1], q[13], q[5];
ccz q[11], q[3], q[0];
c3sx q[9], q[7], q[8], q[10];
rccx q[3], q[4], q[5];
c3sx q[8], q[2], q[10], q[9];
rccx q[11], q[6], q[0];
x q[1];
ccx q[13], q[14], q[12];
tdg q[7];
rccx q[5], q[13], q[11];
ccx q[3], q[4], q[1];
ccx q[6], q[14], q[8];
rzz(1.235795315994922) q[2], q[12];
rccx q[9], q[10], q[0];
c3sx q[6], q[7], q[11], q[4];
rcccx q[0], q[14], q[9], q[1];
ccx q[8], q[13], q[5];
rccx q[12], q[2], q[3];
cswap q[4], q[7], q[6];
sdg q[2];
ccx q[11], q[12], q[0];
c3sx q[5], q[1], q[9], q[3];
cswap q[13], q[14], q[10];
crx(4.661518257996297) q[0], q[9];
rccx q[7], q[11], q[3];
ccz q[6], q[10], q[4];
ry(5.953003268671007) q[8];
p(4.095685186819329) q[14];
ccx q[13], q[5], q[2];
iswap q[1], q[12];
u2(0.1642653119697327, 5.781084714237886) q[7];
ccz q[10], q[3], q[13];
t q[4];
rcccx q[14], q[9], q[11], q[5];
r(4.067218134896907, 3.7119380821657155) q[8];
rx(1.9164065388485196) q[6];
cswap q[1], q[0], q[12];
ccz q[5], q[14], q[9];
rzx(3.7018378089427872) q[8], q[4];
ccx q[11], q[7], q[10];
p(5.286775965557349) q[6];
id q[1];
rccx q[3], q[13], q[0];
p(5.576594942738211) q[12];
h q[12];
c3sx q[6], q[13], q[5], q[0];
ccz q[3], q[14], q[9];
ccz q[7], q[2], q[8];
rccx q[11], q[4], q[10];
r(3.7780850474994696, 2.5590559164525426) q[4];
id q[13];
cswap q[0], q[1], q[7];
ccx q[11], q[2], q[14];
rcccx q[3], q[10], q[9], q[12];
ccz q[5], q[8], q[6];
ccx q[5], q[0], q[4];
ccz q[1], q[9], q[14];
U(6.244110042471542, 0.8403402505495879, 6.147225223969623) q[10];
c3sx q[8], q[3], q[13], q[7];
cswap q[6], q[12], q[2];
ry(1.2695725188757634) q[6];
ccx q[7], q[1], q[0];
z q[8];
csdg q[4], q[5];
rccx q[12], q[14], q[9];
x q[10];
x q[2];
rccx q[13], q[3], q[11];
barrier q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11], q[12], q[13], q[14];
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
meas[11] = measure q[11];
meas[12] = measure q[12];
meas[13] = measure q[13];
meas[14] = measure q[14];
