import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# 📁 Neuer Speicherort der Messdaten
base_dir = "/home/tomas/PycharmProjects/NetzePS_A1/measurements"
good_dir = os.path.join(base_dir, "good_reception")
bad_dir = os.path.join(base_dir, "bad_reception")

# 📂 Ordner für das Diagramm erstellen
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# 🔄 Lade alle CSV-Dateien für beide Messreihen
good_files = sorted(glob.glob(f"{good_dir}/tcp_data_*.csv"))
bad_files = sorted(glob.glob(f"{bad_dir}/tcp_data_*.csv"))

# 📊 Diagramm mit zwei Subplots erstellen
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# ✅ Diagramm für gute WLAN-Verbindung
for i, file in enumerate(good_files, start=1):
    df = pd.read_csv(file, sep="\t", names=["Time", "TCP_Seq"])
    df["Time"] = pd.to_numeric(df["Time"], errors="coerce")
    df["TCP_Seq"] = pd.to_numeric(df["TCP_Seq"], errors="coerce")
    df = df.dropna()
    axes[0].plot(df["Time"], df["TCP_Seq"], marker="o", linestyle="-", label=f"Messung {i}")

axes[0].set_title("Gute WLAN-Verbindung")
axes[0].set_xlabel("Zeit (s)")
axes[0].set_ylabel("TCP-Sequenznummer")
axes[0].legend()
axes[0].grid()

# 🚨 Diagramm für schlechte WLAN-Verbindung
for i, file in enumerate(bad_files, start=1):
    df = pd.read_csv(file, sep="\t", names=["Time", "TCP_Seq"])
    df["Time"] = pd.to_numeric(df["Time"], errors="coerce")
    df["TCP_Seq"] = pd.to_numeric(df["TCP_Seq"], errors="coerce")
    df = df.dropna()
    axes[1].plot(df["Time"], df["TCP_Seq"], marker="o", linestyle="-", label=f"Messung {i}")

axes[1].set_title("Schlechte WLAN-Verbindung")
axes[1].set_xlabel("Zeit (s)")
axes[1].legend()
axes[1].grid()

# 🎨 Layout anpassen
plt.tight_layout()

# 💾 Diagramm speichern
output_path = os.path.join(output_dir, "tcp_comparison.png")
plt.savefig(output_path, dpi=300)
print(f"✅ Diagramm gespeichert als: {output_path}")

# 📊 Diagramm anzeigen
plt.show()
