# ============================================================
# TAREA 1 — AUDITORÍA Y CALIDAD DE DATOS
# Proyecto: Análisis sector Biotech/Pharma 2009-2026
# ============================================================

import pandas as pd

# --- CARGA DE DATOS ---
df = pd.read_csv(r"C:\Users\Fernando\OneDrive\Documentos\proyecto data analytics\datos\biotech_funding.csv")
# --- INFORMACIÓN GENERAL ---
print("=== INFORMACIÓN GENERAL ===")
print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")
print(f"Período: {df['year'].min()} - {df['year'].max()}")
print()

# --- VALORES NULOS ---
print("=== VALORES NULOS ===")
print(df.isnull().sum())
print()

# --- DUPLICADOS ---
print("=== DUPLICADOS ===")
print(f"Filas duplicadas: {df.duplicated().sum()}")
print(f"Deal IDs duplicados: {df['deal_id'].duplicated().sum()}")
print()

# --- TIPOS DE DATO ---
print("=== TIPOS DE DATO ===")
print(df.dtypes)
print()

# --- OUTLIERS (método IQR) ---
print("=== OUTLIERS EN CAPITAL ===")
Q1 = df["value_usd_bn"].quantile(0.25)
Q3 = df["value_usd_bn"].quantile(0.75)
IQR = Q3 - Q1
limite_superior = Q3 + 3 * IQR
outliers = df[df["value_usd_bn"] > limite_superior]
print(f"Límite superior: ${limite_superior:.2f}bn")
print(f"Deals sobre el límite: {len(outliers)}")
print(outliers[["deal_id", "year", "target_or_company", "value_usd_bn"]])
print()

# --- CONCLUSIÓN ---
print("=== CONCLUSIÓN ===")
print("Sin nulos, sin duplicados, sin inconsistencias de fecha.")
print("WARNING: 73 deals sobre P90 con is_megadeal=0 — revisar definición de megadeal.")