from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"; OUT.mkdir(exist_ok=True)
df = pd.read_csv(ROOT/"data"/"pengunjung.csv")
fig, ax = plt.subplots(figsize=(8, 4.8))
bars = ax.bar(df["hari"], df["jumlah_pengunjung"])
ax.set_title("Jumlah Pengunjung Perpustakaan per Hari")
ax.set_xlabel("Hari"); ax.set_ylabel("Jumlah pengunjung")
ax.bar_label(bars, padding=3)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
fig.tight_layout()
path = OUT/"pengunjung_per_hari.png"
fig.savefig(path, dpi=160); plt.close(fig)
print(df.to_string(index=False))
print(f"Grafik tersimpan: {path}")
