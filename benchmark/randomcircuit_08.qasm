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
gate dcx _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_0;
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
bit[8] meas;
qubit[8] q;
cswap q[6], q[7], q[5];
t q[1];
ccz q[2], q[0], q[3];
t q[2];
c3sx q[0], q[7], q[6], q[1];
dcx q[5], q[4];
cu(2.1332392738715247, 0.9334849134188741, 2.871537495561712, 2.7511828987678966) q[4], q[5];
tdg q[0];
t q[2];
cry(3.607915524002728) q[1], q[6];
ch q[3], q[5];
rccx q[1], q[7], q[0];
cswap q[4], q[6], q[2];
rccx q[5], q[3], q[0];
c3sx q[7], q[6], q[4], q[1];
ccz q[5], q[4], q[3];
cswap q[2], q[1], q[7];
u3(1.5699311213649152, 2.6845301397458154, 4.966942791122286) q[3];
cswap q[2], q[7], q[0];
ccx q[4], q[6], q[5];
ry(3.3401519228349494) q[1];
ch q[1], q[7];
ccx q[5], q[2], q[0];
tdg q[6];
cp(2.510079506040741) q[2], q[1];
cswap q[4], q[5], q[6];
ccx q[0], q[3], q[7];
ccx q[2], q[5], q[0];
ccz q[3], q[1], q[7];
cy q[1], q[3];
c3sx q[4], q[7], q[2], q[5];
rccx q[2], q[6], q[3];
u2(0.12608146472089976, 5.306484114352285) q[0];
z q[5];
ccx q[4], q[7], q[1];
cswap q[3], q[2], q[5];
ccx q[1], q[0], q[4];
ryy(0.6403822025770108) q[7], q[6];
cswap q[0], q[1], q[4];
ccx q[2], q[7], q[5];
cx q[6], q[3];
rcccx q[6], q[5], q[3], q[0];
cswap q[7], q[4], q[1];
sxdg q[2];
rcccx q[5], q[6], q[4], q[3];
rccx q[1], q[0], q[7];
barrier q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
meas[5] = measure q[5];
meas[6] = measure q[6];
meas[7] = measure q[7];
