import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
visitatori = np.random.normal(2000, 500, 365)
visitatori = visitatori.astype(int)

print(visitatori[:10])

# generiamo 365 date con distanza da un giorno uno dalle altre
date = pd.date_range(start="2025-01-01", periods=365, freq="D")

# crea il dataframe con le date come indice
df = pd.DataFrame({"visitatori": visitatori}, index=date)

# assegnamo data al nome dell'indice
df.index.name = "data"

# stampiamo prime 5 righe
print(df.head())

# media e deviazione standard per ogni mese
statistiche = df.resample("MS")["visitatori"].agg(["mean", "std"])

# arrotondiamo a 2 decimali
statistiche = statistiche.round(2)

# rinominiamo le colonne
statistiche.columns = ["media", "deviazione_standard"]

# stampiamo le statistiche mensili
print(statistiche)

# dimensioni 12x5 per il grafico
plt.figure(figsize=(12, 5))

# creiamo le linee usando date per X e visitatori Y
plt.plot(df.index, df["visitatori"], label="Visitatori giornalieri")

plt.title("Visitatori giornalieri del parco")

plt.xlabel("Data")

plt.ylabel("Numero di visitatori")

plt.grid(True)

plt.legend()

plt.show()
