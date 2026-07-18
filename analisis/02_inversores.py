# ============================================================
# TAREA 2 — RANKING DE INVERSORES Y ADQUIRENTES
# Proyecto: Análisis sector Biotech/Pharma 2009-2026
# ============================================================

import pandas as pd

# --- CARGA DE DATOS ---
df = pd.read_csv(r"C:\Users\Fernando\OneDrive\Documentos\proyecto data analytics\datos\biotech_funding.csv")

# --- RANKING POR CAPITAL Y DEALS ---
capital = df.groupby("acquirer_or_investors")["value_usd_bn"].sum()
deals = df.groupby("acquirer_or_investors")["deal_id"].count()

ranking = pd.DataFrame({
    "capital_usd_bn": capital,
    "cantidad_deals": deals
})

ranking["promedio_por_deal"] = ranking["capital_usd_bn"] / ranking["cantidad_deals"]
ranking = ranking.sort_values("capital_usd_bn", ascending=False)

print("=== RANKING COMPLETO DE INVERSORES ===")
print(ranking)
print()

# --- CONCENTRACIÓN TOP 5 ---
total_capital = df["value_usd_bn"].sum()
top5_capital = ranking["capital_usd_bn"].head(5).sum()
porcentaje_top5 = (top5_capital / total_capital) * 100

print("=== CONCENTRACIÓN ===")
print(f"Capital total del dataset: ${total_capital:.1f}bn")
print(f"Capital top 5 inversores: ${top5_capital:.1f}bn")
print(f"El top 5 controla el {porcentaje_top5:.1f}% del capital total")
print()

# --- DOS MUNDOS: PHARMA VS VC ---
vc = ["Flagship Pioneering", "Third Rock Ventures", "Sofinnova Investments",
      "ARCH Venture Partners", "F-Prime Capital", "Bain Capital Life Sciences",
      "OrbiMed", "Versant Ventures", "GV (Google Ventures)", "Atlas Venture",
      "Polaris Partners", "a16z Bio", "RA Capital", "VC syndicate"]

pharma = ["AbbVie", "BMS", "Sanofi", "Roche", "AstraZeneca", "Eli Lilly",
          "Pfizer", "Amgen", "J&J", "Actavis", "Gilead", "Merck",
          "GSK", "Novartis", "Teva", "Shire", "Bayer", "Celgene", "Vertex"]

capital_vc = df[df["acquirer_or_investors"].isin(vc)]["value_usd_bn"].sum()
capital_pharma = df[df["acquirer_or_investors"].isin(pharma)]["value_usd_bn"].sum()

print("=== PHARMA VS VC ===")
print(f"Capital mundo VC:     ${capital_vc:.1f}bn")
print(f"Capital mundo Pharma: ${capital_pharma:.1f}bn")
print(f"Pharma mueve {capital_pharma/capital_vc:.1f}x mas capital que VC")
print()

# --- CASO EXTREMO: ACTAVIS ---
print("=== CASO EXTREMO: ACTAVIS ===")
actavis = df[df["acquirer_or_investors"] == "Actavis"]
print(actavis[["year", "deal_type", "target_or_company", "value_usd_bn"]])

print()
print("=== CONCLUSIÓN ===")
print("34 inversores para 1208 deals — mercado concentrado.")
print("Top 5 controla el 42% del capital total.")
print("Pharma mueve 8x mas capital que VC.")
print("Actavis: $70.5bn en un solo deal (compra de Allergan, 2014).")