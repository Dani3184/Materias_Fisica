import pandas as pd
import matplotlib.pyplot as plt

# === Cargar datos ===
data = pd.read_csv("datos_combinados2.csv", parse_dates=["Hora"])

# === Crear figura ===
fig, ax1 = plt.subplots(figsize=(12, 6))

# --- Eje principal (ax1) para Media de Cuentas ---
ax1.plot(data["Hora"], data["Media_Cuentas"], color="blue", marker="o", label="Media Cuentas")
# ax1.fill_between(data["Hora"],
#                  data["Media_Cuentas"] - data["Desviacion_Cuentas"],
#                  data["Media_Cuentas"] + data["Desviacion_Cuentas"],
#                  color="blue", alpha=0.2, label="± Desviación")
ax1.set_ylabel("Cuentas (Media ± σ)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# --- Eje secundario (ax2) para Temperatura ---
ax2 = ax1.twinx()
ax2.plot(data["Hora"], data["Temperatura"], color="red", marker="^", label="Temperatura (°C)")
ax2.set_ylabel("Temperatura (°C)", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# === Título y formato ===
plt.title("Evolución de Cuentas y Temperatura")
fig.autofmt_xdate()

# === Combinar leyendas ===
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("cuentasTemp.jpg")
plt.show()
