#!/bin/bash

algorithms=("randomcircuit" "qft" "vqe_real_amp" "qaoa" "grover" "hhl")

output_dir="./benchmark"
mkdir -p "$output_dir"

# Loop through each algorithm and qubit range (2 to 20)
for alg in "${algorithms[@]}"; do
    for qbit_num in {2..20}; do
	formated_num=$(printf "%02d" "$qbit_num")
        output_file="$output_dir/${alg}_${formated_num}.qasm"
        echo "Running: mqt-bench --level alg --algorithm $alg --num-qubits $qbit_num --output-format qasm3 > $output_file"
        # command
        mqt-bench --level alg --algorithm "$alg" --num-qubits "$qbit_num" --output-format qasm3 > "$output_file" 2>&1
        if [ $? -eq 0 ]; then
            echo "Generated: $output_file"
        else
            echo "Error generating: $output_file"
        fi
    done
done

echo "Done"
