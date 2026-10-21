import random

import pandas as pd

# 1. Creare un DataFrame con dati casuali

nomi = [
    "Luca",
    "Marco",
    "Anna",
    "Giulia",
    "Sara",
    "Paolo",
    "Elena",
    "Andrea",
    "Marta",
    "Sofia",
]

citta = ["Verona", "Milano", "Torino", "Roma", "Padova"]

righe = []

for i in range(15):
    persona = {
        "Nome": random.choice(nomi),
        "Età": random.randint(0, 90),
        "Città": random.choice(citta),
        "Salario": random.randint(1200, 5000),
    }

    righe.append(persona)

# Aggiungo una riga duplicata per testare il punto 5
righe.append(righe[2].copy())

df = pd.DataFrame(righe)

# Inserisco valori mancanti per testare il punto 6
df.loc[3, "Età"] = None
df.loc[7, "Età"] = None
df.loc[5, "Salario"] = None
df.loc[9, "Salario"] = None


# 2. Visualizzare le prime e le ultime cinque righe

print("PRIME CINQUE RIGHE")
print(df.head())

print("ULTIME CINQUE RIGHE")
print(df.tail())


# 3. Visualizzare il tipo di dati di ciascuna colonna

print("TIPI DI DATI")
print(df.dtypes)


# 4. Calcolare le statistiche descrittive di base

print("STATISTICHE DESCRITTIVE")

print(df[["Età", "Salario"]].agg(["mean", "median", "std"]))


# 5. Identificare e rimuovere i duplicati

print("RIGHE DUPLICATE")
print(df[df.duplicated()])

df = df.drop_duplicates()
df = df.reset_index(drop=True)

print("DATAFRAME SENZA DUPLICATI")
print(df)


# 6. Sostituire i valori mancanti con la mediana

print("VALORI MANCANTI PRIMA")
print(df.isnull().sum())

df["Età"] = df["Età"].fillna(df["Età"].median())
df["Salario"] = df["Salario"].fillna(df["Salario"].median())

print("VALORI MANCANTI DOPO")
print(df.isnull().sum())


# 7. Aggiungere la colonna "Categoria Età"


def categoria_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"


df["Categoria Età"] = df["Età"].apply(categoria_eta)

print("DATAFRAME FINALE")
print(df)
