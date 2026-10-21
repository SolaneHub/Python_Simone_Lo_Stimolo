import pandas as pd

df_scv = pd.read_csv("21-10-2026/studenti.csv")

print(df_scv)

df_scv["Sesso"] = ["F", "M", "F", "F", "M", "F", "F", "M", "F", "F"]

print(df_scv["voto"].mean())

print(df_scv["voto"].max())

print(df_scv[df_scv["voto"] > 7])

df_scv.to_csv("21-10-2026/studenti_aggiornati.csv", index=False)
