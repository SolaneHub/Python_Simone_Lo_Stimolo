import matplotlib.pyplot as plt
import pandas as pd

df_catalogo = pd.read_csv("23-10-2026/test_pratico/candy-data.csv")
df_vendite = pd.read_csv("23-10-2026/test_pratico/candy-vendite.csv")

# stampo le dimensioni dei nostri dataframe
print("df_catalogo:", df_catalogo.shape)
print("df_vendite:", df_vendite.shape)

# stampo tutte le informazioni riguardanti il dataframe, numero colonne, valori non nulli e tipi di dati all'interno di esse
df_catalogo.info()
df_vendite.info()

# stampo per ogni colonna se esistono valori vuoti
print(df_catalogo.isna().sum())
print(df_vendite.isna().sum())

# stampo un describe, quindi tutte le colonne con associato il numero di righe, media, mediana, valori massimi e minimi
print(df_catalogo.describe().to_string())
print(df_vendite.describe().to_string())

# controllo se ci siano o meno righe duplicate
print("Righe duplicate in df_catalogo:", df_catalogo.duplicated().sum())
print("Righe duplicate in df_vendite:", df_vendite.duplicated().sum())

# pulizia minima dei dati, togliamo spazi vuoti
df_catalogo["competitorname"] = df_catalogo["competitorname"].str.strip()
df_vendite["competitorname"] = df_vendite["competitorname"].str.strip()

# togliamo i prodotti di prova
prodotti_test = ["Candy Test A", "Candy Test B", "Candy Test C"]
df_vendite_pulito = df_vendite[~df_vendite["competitorname"].isin(prodotti_test)]

# teniamo i dolci del catalogo e ci uniamo le vendite
df_finale = pd.merge(df_catalogo, df_vendite_pulito, on="competitorname", how="left")

# ci sono dei prodotti che non sono presenti nella tabella delle vendite, impostiamo i loro valori a 0
df_finale["unita_vendute"] = df_finale["unita_vendute"].fillna(0)

# dataset finale
print("Dimensioni dataset finale:", df_finale.shape)
print(df_finale[["competitorname", "unita_vendute"]].to_string())

# facciamo uno studio sui 5 prodotti più venduti
top5 = df_finale.sort_values(by="unita_vendute", ascending=False).head(5)

# creiamo un grafico a torta
plt.figure(figsize=(7, 7))
plt.pie(
    top5["unita_vendute"],
    labels=top5["competitorname"],
    autopct="%1.1f%%",
    startangle=90,
)

plt.title("Quota vendite dei Top 5 dolci")
plt.tight_layout()
plt.show()
