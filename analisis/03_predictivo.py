# ============================================================
# TAREA 3 — MODELO PREDICTIVO 2026
# Proyecto: Análisis sector Biotech/Pharma 2009-2026
# ============================================================

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# --- CARGA DE DATOS ---
df = pd.read_csv(r"C:\Users\Fernando\OneDrive\Documentos\proyecto data analytics\datos\biotech_funding.csv")

# --- PREPARAR DATOS ANUALES ---
por_año = df.groupby("year").agg(
    cantidad_deals=("deal_id", "count"),
    capital_usd_bn=("value_usd_bn", "sum")
).reset_index()

# Sacar 2026 porque está incompleto
datos = por_año[por_año["year"] < 2026]

print("=== DATOS HISTÓRICOS ===")
print(datos)
print()

# --- MODELO REGRESIÓN LINEAL (deals) ---
X = datos[["year"]]
y_deals = datos["cantidad_deals"]

modelo_deals = LinearRegression()
modelo_deals.fit(X, y_deals)
pred_deals_regresion = modelo_deals.predict([[2026]])[0]

# --- MÉTODO HONESTO: PROMEDIO ÚLTIMOS 3 AÑOS ---
# Usamos promedio en lugar de regresión porque:
# - El pico de 2021 (pandemia) distorsiona la línea recta
# - Los últimos 3 años reflejan mejor la tendencia real post-boom
ultimos_3 = datos[datos["year"] >= 2023]

pred_deals_honesto = ultimos_3["cantidad_deals"].mean()
pred_capital_honesto = ultimos_3["capital_usd_bn"].mean()

print("=== PREDICCIÓN 2026 ===")
print(f"Regresión lineal (sesgada por 2021): {pred_deals_regresion:.0f} deals")
print(f"Promedio 2023-2025 (método honesto): {pred_deals_honesto:.0f} deals")
print(f"Capital estimado 2026:               ${pred_capital_honesto:.1f}bn")
print()

print("=== CONCLUSIÓN ===")
print("El pico de 2021 (133 deals) fue un evento excepcional por pandemia.")
print("La tendencia real post-boom se estabiliza entre 77-95 deals por año.")
print(f"Estimación conservadora 2026: ~{pred_deals_honesto:.0f} deals, ~${pred_capital_honesto:.0f}bn capital.")
print("Rango probable: 74-94 deals.")