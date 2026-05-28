Traceback (most recent call last):
  File "/u/halle/wraf/home_at/qml-env/bin/mqt-bench", line 6, in <module>
    sys.exit(main())
             ^^^^^^
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/cli.py", line 121, in main
    circuit = get_benchmark(
              ^^^^^^^^^^^^^^
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/benchmark_generation.py", line 546, in get_benchmark
    return get_benchmark_alg(
           ^^^^^^^^^^^^^^^^^^
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/benchmark_generation.py", line 220, in get_benchmark_alg
    qc = _get_circuit(benchmark, circuit_size, random_parameters, **kwargs)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/benchmark_generation.py", line 78, in _get_circuit
    qc = create_circuit(benchmark, circuit_size, **kwargs)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/benchmarks/__init__.py", line 128, in create_circuit
    factory = _get_factory(benchmark_name)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/benchmarks/__init__.py", line 98, in _get_factory
    _ensure_loaded(benchmark_name)
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/benchmarks/__init__.py", line 69, in _ensure_loaded
    raise ValueError(msg)
ValueError: 'vqe' is not a supported benchmark. Available benchmarks: ['ae', 'bmw_quark_cardinality', 'bmw_quark_copula', 'bv', 'cdkm_ripple_carry_adder', 'dj', 'draper_qft_adder', 'full_adder', 'ghz', 'ghz_dynamic', 'graphstate', 'grover', 'half_adder', 'hhl', 'hrs_cumulative_multiplier', 'modular_adder', 'multiplier', 'qaoa', 'qft', 'qftentangled', 'qnn', 'qpeexact', 'qpeinexact', 'qwalk', 'randomcircuit', 'rg_qft_multiplier', 'seven_qubit_steane_code', 'shor', 'shors_nine_qubit_code', 'vbe_ripple_carry_adder', 'vqe_real_amp', 'vqe_su2', 'vqe_two_local', 'wstate']
