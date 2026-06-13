from abc import ABC, abstractmethod
import time
import statistics
import psutil
import os
from typing import Any, Dict, List
from dataclasses import dataclass
from datetime import datetime

from mqt.qcec.pyqcec import EquivalenceCheckingManager


@dataclass
class SingleRunStatistics:
    # Timing Metrics
    import_time_ms: float
    transpilation_time_ms: float
    verify_time_ms: float

    # Memory Metrics (Process Level - RSS)
    import_memory_mb: float
    transpilation_memory_mb: float
    verify_memory_mb: float

    # Circuit Metrics
    circuit_width: int
    original_gate_count: int
    transpiled_gate_count: int
    depth_transpiled: int

    transpiled_exact_gates:str

    # Metadata
    timestamp: str
    equivalent: EquivalenceCheckingManager.Results

    def to_dict(self) -> Dict[str, Any]:
        return {
            'import_time_ms': self.import_time_ms,
            'transpilation_time_ms': self.transpilation_time_ms,
            'verify_time_ms': self.verify_time_ms,
            'import_memory_mb': self.import_memory_mb,
            'transpilation_memory_mb': self.transpilation_memory_mb,
            'verify_memory_mb': self.verify_memory_mb,
            'circuit_width': self.circuit_width,
            'original_gate_count': self.original_gate_count,
            'transpiled_gate_count': self.transpiled_gate_count,
            'transpiled_exact' : self.transpiled_exact_gates,
            'depth_transpiled': self.depth_transpiled,
            'timestamp': self.timestamp,
            'equivalent': self.equivalent.json(),
        }


@dataclass
class RunStatistics:
    # Metadata
    sdk_name: str
    timestamp: str
    algorithm: str
    qubits: int
    # Timing Metrics
    avg_import_time_ms: float
    avg_transpilation_time_ms: float
    avg_verify_time_ms: float

    # Memory Metrics (Process Level - RSS)
    avg_import_memory_mb: float
    avg_transpilation_memory_mb: float
    avg_verify_memory_mb: float

    # Circuit Metrics
    avg_circuit_width: float
    avg_original_gate_count: float
    avg_transpiled_gate_count: float
    depth_original: float
    avg_depth_transpiled: float

    # Runs
    runs: int
    runs_stats: List[SingleRunStatistics]
    failed_transpilations: int

    def to_dict(self) -> Dict[str, Any]:
        """Convert statistics to dictionary for JSON serialization"""
        return {
            'sdk_name': self.sdk_name,
            'timestamp': self.timestamp,
            'algorithm': self.algorithm,
            'qubits': self.qubits,
            'failed_transpilations': self.failed_transpilations,
            'timing_metrics': {
                'avg_import_time_ms': self.avg_import_time_ms,
                'avg_transpilation_time_ms': self.avg_transpilation_time_ms,
                'avg_verify_time_ms': self.avg_verify_time_ms,
            },
            'memory_metrics': {
                'avg_import_memory_mb': self.avg_import_memory_mb,
                'avg_transpilation_memory_mb': self.avg_transpilation_memory_mb,
                'avg_verify_memory_mb': self.avg_verify_memory_mb,
            },
            'circuit_metrics': {
                'avg_original_gate_count': self.avg_original_gate_count,
                'avg_transpiled_gate_count': self.avg_transpiled_gate_count,
                'depth_original': self.depth_original,
                'avg_depth_transpiled': self.avg_depth_transpiled,
            },
            'runs': self.runs,
            'runs_stats': [run_stat.to_dict() for run_stat in self.runs_stats]
        }


class QuantumTranspilerTestSuite(ABC):
    """Abstract base class for quantum transpiler testing across different SDKs"""

    sdk_name: str

    @abstractmethod
    def import_qasm(self, qasm_code: str) -> Any:
        """Import QASM code into SDK format"""
        pass

    @abstractmethod
    def transpile(self, circuit: Any) -> Any:
        """Transpile the circuit"""
        pass

    @abstractmethod
    def verify_circuit(self, original: Any, transpiled: Any) -> EquivalenceCheckingManager.Results:
        """Verify equivalence of original and transpiled circuits"""
        pass

    @abstractmethod
    def get_circuit_metrics(self, stats: SingleRunStatistics, original: Any, transpiled: Any):
        """
        Extract circuit metrics and update the stats object.
        Should set:
            stats.original_gate_count
            stats.transpiled_gate_count
            stats.depth_transpiled
            stats.circuit_width
        """
        pass

    def _get_memory_usage(self) -> float:
        """Get current process memory usage in MB"""
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024

    def run(self, qasm_code: str) -> SingleRunStatistics:
        """Execute a single transpilation run with metrics collection"""
        # Track memory before import
        memory_before_import = self._get_memory_usage()
        import_start = time.time()
        try:
            original_circuit = self.import_qasm(qasm_code)
        except Exception as e:
            raise RuntimeError(f"Import failed: {str(e)}")
        import_time = (time.time() - import_start) * 1000
        import_memory = self._get_memory_usage() - memory_before_import

        # Transpilation phase
        memory_before_transpile = self._get_memory_usage()
        transpile_start = time.time()
        try:
            transpiled_circuit = self.transpile(original_circuit)
        except Exception as e:
            raise RuntimeError(f"Transpilation failed: {str(e)}")
        transpile_time = (time.time() - transpile_start) * 1000
        transpile_memory = self._get_memory_usage() - memory_before_transpile

        # Verification phase

        memory_before_verify = self._get_memory_usage()
        verify_start = time.time()
        try:
            equivalent = self.verify_circuit(original_circuit, transpiled_circuit)
        except Exception as e:
            print(f"Verification failed: {str(e)}")
            equivalent = EquivalenceCheckingManager.Results()

        verify_time = (time.time() - verify_start) * 1000
        verify_memory = self._get_memory_usage() - memory_before_verify

        # Initialize with default metrics
        stats = SingleRunStatistics(
            import_time_ms=import_time,
            transpilation_time_ms=transpile_time,
            verify_time_ms=verify_time,
            import_memory_mb=import_memory,
            transpilation_memory_mb=transpile_memory,
            verify_memory_mb=verify_memory,
            timestamp=datetime.now().isoformat(),
            equivalent=equivalent,
            original_gate_count=0,
            transpiled_gate_count=0,
            transpiled_exact_gates="",
            depth_transpiled=0,
            circuit_width=0
        )

        # Get circuit metrics
        self.get_circuit_metrics(stats, original_circuit, transpiled_circuit)

        return stats

    def test(self, path: str, runs: int = 5) -> RunStatistics:
        """
        Execute full test suite on QASM file

        Args:
            path: Path to QASM file
            runs: Number of runs to execute

        Returns:
            RunStatistics with aggregated results
        """
        try:
            with open(path, 'r') as f:
                qasm_code = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"QASM file not found: {path}")

        algorithm = os.path.splitext(os.path.basename(path))[0]
        try:
            qubits = self._extract_qubit_count(qasm_code)
        except Exception as e:
            qubits = 0
            print(f"Failed to extract qubits: {e}")

        runs_stats: List[SingleRunStatistics] = []
        failed_count = 0

        print(f"Running {runs} transpilation tests on {algorithm}...")

        for i in range(runs):
            try:
                stats = self.run(qasm_code)

                if stats.equivalent:
                    status = str(stats.equivalent.equivalence)
                else:
                    failed_count += 1
                    status =  "Failure"
                print(f"  Run {i + 1}/{runs}: {status} "
                      f"(import: {stats.import_time_ms:.2f}ms, "
                      f"transpile: {stats.transpilation_time_ms:.2f}ms, "
                      f"gates: {stats.transpiled_exact_gates})")

                runs_stats.append(stats)

            except Exception as e:
                print(f"  Run {i + 1}/{runs}: FAILED - {str(e)}")
                failed_count += 1

        aggregated_stats = self._aggregate_statistics(
            runs_stats=runs_stats,
            sdk_name=self.sdk_name,
            algorithm=algorithm,
            qubits=qubits,
            failed_transpilations=failed_count
        )

        return aggregated_stats

    @abstractmethod
    def _extract_qubit_count(self, circuit: Any) -> int:
        """Get circuit's qubit count"""
        pass

    def _aggregate_statistics(
            self,
            runs_stats: List[SingleRunStatistics],
            sdk_name: str,
            algorithm: str,
            qubits: int,
            failed_transpilations: int
    ) -> RunStatistics:
        """Aggregate individual run statistics"""

        if not runs_stats:
            return RunStatistics(
                sdk_name=sdk_name,
                timestamp=datetime.now().isoformat(),
                algorithm=algorithm,
                qubits=0,
                failed_transpilations=failed_transpilations,
                # Timing
                avg_import_time_ms=0,
                avg_transpilation_time_ms=0,
                avg_verify_time_ms=0,
                # Memory
                avg_import_memory_mb=0,
                avg_transpilation_memory_mb=0,
                avg_verify_memory_mb=0,
                # Circuit
                avg_circuit_width=0,
                avg_original_gate_count=0,
                avg_transpiled_gate_count=0,
                depth_original=0,
                avg_depth_transpiled=0,
                runs=0,
                runs_stats=runs_stats
            )

        # Timing metrics
        import_times = [s.import_time_ms for s in runs_stats]
        transpile_times = [s.transpilation_time_ms for s in runs_stats]
        verify_times = [s.verify_time_ms for s in runs_stats]

        # Memory metrics
        import_mem = [s.import_memory_mb for s in runs_stats]
        transpile_mem = [s.transpilation_memory_mb for s in runs_stats]
        verify_mem = [s.verify_memory_mb for s in runs_stats]

        # Circuit metrics
        original_gate_counts = [s.original_gate_count for s in runs_stats]
        transpiled_gate_counts = [s.transpiled_gate_count for s in runs_stats]
        depths = [s.depth_transpiled for s in runs_stats]
        circuit_widths = [s.circuit_width for s in runs_stats]

        total_runs = len(runs_stats) + failed_transpilations

        return RunStatistics(
            sdk_name=sdk_name,
            timestamp=datetime.now().isoformat(),
            algorithm=algorithm,
            qubits=qubits,
            failed_transpilations=failed_transpilations,
            # Timing
            avg_import_time_ms=statistics.mean(import_times),
            avg_transpilation_time_ms=statistics.mean(transpile_times),
            avg_verify_time_ms=statistics.mean(verify_times),
            # Memory
            avg_import_memory_mb=statistics.mean(import_mem),
            avg_transpilation_memory_mb=statistics.mean(transpile_mem),
            avg_verify_memory_mb=statistics.mean(verify_mem),
            # Circuit
            avg_circuit_width=statistics.mean(circuit_widths),
            avg_original_gate_count=statistics.mean(original_gate_counts),
            avg_transpiled_gate_count=statistics.mean(transpiled_gate_counts),
            depth_original=depths[0] if depths else 0,
            avg_depth_transpiled=statistics.mean(depths),
            runs=total_runs,
            runs_stats=runs_stats
        )