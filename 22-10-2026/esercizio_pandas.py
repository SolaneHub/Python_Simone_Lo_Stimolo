import numpy as np
import pandas as pd

# Seed per rendere i dati prevedibili ad ogni esecuzione
np.random.seed(42)

# Valori random
n_righe = 150
date_disponibili = pd.date_range(start="2026-10-01", end="2026-10-31", freq="D")
elenco_citta = ["Milano", "Roma", "Napoli"]
elenco_prodotti = ["Laptop", "Smartphone", "Tablet"]

# Costruzione del DataFrame
df = pd.DataFrame(
    {
        "Data": np.random.choice(date_disponibili, size=n_righe),
        "Città": np.random.choice(elenco_citta, size=n_righe),
        "Prodotto": np.random.choice(elenco_prodotti, size=n_righe),
        "Vendite": np.round(
            np.random.uniform(100.0, 1500.0, size=n_righe), 2 # Genera colonna di valori arrotondata a 2 cifre decimali
        ),
    }
)

# Ordinamento per data per facilitare la lettura
df = df.sort_values("Data").reset_index(drop=True) # reset_index per reimpostare il nuovo ordine degli indici modificato dal sort, drop per eliminare il vecchio indice

print(df.head())

# Creiamo una matrice bidimensionale (Città x Prodotto) con contenuto "Vendite", aggfunc per la media, e arrotondiamo i valori a 2 cifre decimali
pivot_medie = df.pivot_table(
    values="Vendite", index="Città", columns="Prodotto", aggfunc="mean"
).round(2)

print("--- Vendite Medie per Città e Prodotto (€) ---")
print(pivot_medie)

# group.by per separare Laptop/Smartphone/Tablet e concentriamo il calcolo su Vendite
# sum, sommiamo tutti i valori di vendita di ciascun gruppo
# reset_index per togliere Prodotto come indice, e reimpostarlo a colonna
# sort_values per ordinare per Vendite in ordine decrescente
totale_per_prodotto = (
    df.groupby("Prodotto")["Vendite"]
    .sum()
    .reset_index()  # Trasforma l'indice 'Prodotto' in una colonna normale
    .sort_values(by="Vendite", ascending=False)
)

print("--- Vendite Totali per Prodotto (€) ---")
print(totale_per_prodotto)
