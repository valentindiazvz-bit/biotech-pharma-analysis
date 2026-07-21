# ============================================================
# TAREA 4 — VISUALIZACIONES
# Proyecto: Análisis sector Biotech/Pharma 2009-2026
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# --- CARGA DE DATOS ---
df = pd.read_csv(r"C:\Users\Fernando\OneDrive\Documentos\proyecto data analytics\datos\biotech_funding.csv")

# --- PREPARAR DATOS ---
por_año = df.groupby("year").agg(
    cantidad_deals=("deal_id", "count"),
    capital_usd_bn=("value_usd_bn", "sum")
).reset_index()

# --- GRÁFICO 1: DEALS POR AÑO ---
plt.figure(figsize=(12, 5))
plt.bar(por_año["year"], por_año["cantidad_deals"], color="steelblue")
plt.axhline(y=100, color="red", linestyle="--", label="Barrera 100 deals")
plt.title("Cantidad de deals por año — Biotech/Pharma 2009-2026")
plt.xlabel("Año")
plt.ylabel("Cantidad de deals")
plt.legend()
plt.tight_layout()
plt.savefig(r"C:\Users\Fernando\OneDrive\Documentos\proyecto data analytics\analisis\grafico_deals_por_año.png")
plt.show()
print("Grafico 1 guardado.")

# --- GRÁFICO 2: CAPITAL POR AÑO ---
plt.figure(figsize=(12, 5))
plt.plot(por_año["year"], por_año["capital_usd_bn"], color="steelblue", marker="o")
plt.title("Capital total por año — Biotech/Pharma 2009-2026")
plt.xlabel("Año")
plt.ylabel("Capital (USD bn)")
plt.tight_layout()
plt.savefig(r"C:\Users\Fernando\OneDrive\Documentos\proyecto data analytics\analisis\grafico_capital_por_año.png")
plt.show()
print("Grafico 2 guardado.")

# --- GRÁFICO 3: RANKING DE INVERSORES ---
capital = df.groupby("acquirer_or_investors")["value_usd_bn"].sum().sort_values()

plt.figure(figsize=(10, 10))
plt.barh(capital.index, capital.values, color="steelblue")
plt.title("Capital total por inversor — Biotech/Pharma 2009-2026")
plt.xlabel("Capital (USD bn)")
plt.tight_layout()
plt.savefig(r"C:\Users\Fernando\OneDrive\Documentos\proyecto data analytics\analisis\grafico_inversores.png")
plt.show()
print("Grafico 3 guardado.")

# --- GRÁFICO 4: DEALS POR TIPO ---
por_tipo = df.groupby("deal_type")["deal_id"].count().sort_values()

plt.figure(figsize=(8, 5))
plt.barh(por_tipo.index, por_tipo.values, color="steelblue")
plt.title("Cantidad de deals por tipo")
plt.xlabel("Cantidad")
plt.tight_layout()
plt.savefig(r"C:\Users\Fernando\OneDrive\Documentos\proyecto data analytics\analisis\grafico_tipos.png")
plt.show()
print("Grafico 4 guardado.")

print()
print("=== TODOS LOS GRÁFICOS GUARDADOS ===")