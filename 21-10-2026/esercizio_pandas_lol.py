import sys

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

# 1. Caricare il file CSV e creare un DataFrame
df = pd.read_csv("21-10-2026/lolchamps.csv")

print("DATAFRAME ORIGINALE")
print(df.head())

# 2. Esplorare i dati
print("INFORMAZIONI SUL DATAFRAME")
print(df.info())

print("DIMENSIONI DEL DATAFRAME")
print(df.shape)

print("NOMI DELLE COLONNE")
print(df.columns)

print("VALORI MANCANTI")
print(df.isnull().sum())

print("RIGHE DUPLICATE")
print(df.duplicated().sum())

# 3. Pulire i dati
df.columns = df.columns.str.strip()

df = df.drop_duplicates()

df = df.dropna(subset=["Number", "English Name", "中文名称"])

df["English Name"] = df["English Name"].str.strip()
df["中文名称"] = df["中文名称"].str.strip()

df["Number"] = pd.to_numeric(df["Number"], errors="coerce")

df = df.dropna(subset=["Number"])

df["Number"] = df["Number"].astype(int)

# 4. Creare almeno due nuove colonne
df["Name Length"] = df["English Name"].str.len()

df["Has Chinese Name"] = df["中文名称"].ne("")

# 5. Presentare i dati
print("DATAFRAME PULITO E AGGIORNATO")
print(df.head(10))

print("STATISTICHE DESCRITTIVE")
print(df.describe())

print("CAMPIONI DI DATI")
print(df[["English Name", "Name Length", "Has Chinese Name"]].head(10))

print("NUMERO TOTALE DI CAMPIONI")
print(len(df))

print("DATAFRAME FINALE")
print(df)

# Salvare il risultato in un nuovo CSV
df.to_csv("21-10-2026/lolchamps_clean.csv", index=False, encoding="utf-8-sig")
