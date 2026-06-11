import json
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Wczytanie JSON
with open("results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ekstrakcja danych
rows = []

for item in data:
    rows.append({
        "algorithm": item["algorithm"],
        "qubits": item["qubits"],
        "transpilation_time_ms": item["timing_metrics"]["avg_transpilation_time_ms"],
        "verify_time_ms": item["timing_metrics"]["avg_verify_time_ms"],
        "transpilation_memory_mb": item["memory_metrics"]["avg_transpilation_memory_mb"],
        "verify_memory_mb": item["memory_metrics"]["avg_verify_memory_mb"],
        "gate_count": item["circuit_metrics"]["avg_transpiled_gate_count"],
        "depth": item["circuit_metrics"]["avg_depth_transpiled"]
    })

df = pd.DataFrame(rows)

# Styl naukowy
plt.style.use("default")

# ===== 1. Transpylacja =====
plt.figure(figsize=(8,5))
plt.plot(df["qubits"], df["transpilation_time_ms"], marker="o")
plt.xlabel("Liczba kubitów")
plt.ylabel("Średni czas transpylacji [ms]")
plt.title("Skalowanie czasu transpylacji")
plt.grid(True)
plt.tight_layout()
plt.savefig("transpilation_time.png", dpi=300)
plt.close()

# ===== 2. Weryfikacja =====
plt.figure(figsize=(8,5))
plt.plot(df["qubits"], df["verify_time_ms"], marker="o")
plt.xlabel("Liczba kubitów")
plt.ylabel("Średni czas weryfikacji [ms]")
plt.title("Skalowanie czasu weryfikacji")
plt.grid(True)
plt.tight_layout()
plt.savefig("verify_time.png", dpi=300)
plt.close()

# ===== 3. Pamięć =====
plt.figure(figsize=(8,5))
plt.plot(df["qubits"], df["verify_memory_mb"], marker="o",
         label="Weryfikacja")
plt.plot(df["qubits"], df["transpilation_memory_mb"], marker="s",
         label="Transpylacja")
plt.xlabel("Liczba kubitów")
plt.ylabel("Pamięć [MB]")
plt.title("Zużycie pamięci")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("memory_usage.png", dpi=300)
plt.close()

# ===== 4. Bramy =====
plt.figure(figsize=(8,5))
plt.plot(df["qubits"], df["gate_count"], marker="o")
plt.xlabel("Liczba kubitów")
plt.ylabel("Liczba bramek")
plt.title("Rozmiar obwodu")
plt.grid(True)
plt.tight_layout()
plt.savefig("gate_count.png", dpi=300)
plt.close()

# ===== 5. Głębokość =====
plt.figure(figsize=(8,5))
plt.plot(df["qubits"], df["depth"], marker="o")
plt.xlabel("Liczba kubitów")
plt.ylabel("Głębokość obwodu")
plt.title("Głębokość obwodu po transpylacji")
plt.grid(True)
plt.tight_layout()
plt.savefig("circuit_depth.png", dpi=300)
plt.close()

print(df)