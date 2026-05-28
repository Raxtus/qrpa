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
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/benchmarks/__init__.py", line 129, in create_circuit
    return factory(circuit_size, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/u/halle/wraf/home_at/qml-env/lib/python3.12/site-packages/mqt/bench/benchmarks/hhl.py", line 35, in create_circuit
    raise ValueError(msg)
ValueError: Number of qubits must be at least 3 for HHL.
