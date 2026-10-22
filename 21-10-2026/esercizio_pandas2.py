import pandas as pd

# 1. Creare un dizionario contenente i dati delle vendite
# Ogni chiave rappresenta il nome di una colonna,
# mentre la lista contiene i valori da inserire nella colonna.
dati = {
    "Prodotto": [
        "Laptop",
        "Mouse",
        "Tastiera",
        "Laptop",
        "Monitor",
        "Mouse",
        "Tastiera",
        "Monitor",
        "Laptop",
        "Mouse",
    ],
    "Quantità": [2, 10, 5, 1, 3, 15, 8, 4, 1, 5],
    "Prezzo Unitario": [700, 20, 45, 700, 180, 20, 45, 180, 700, 20],
    "Città": [
        "Milano",
        "Verona",
        "Milano",
        "Torino",
        "Verona",
        "Torino",
        "Roma",
        "Milano",
        "Milano",
        "Roma",
    ],
}

# Trasformare il dizionario in un DataFrame, cioè una tabella di Pandas.
df = pd.DataFrame(dati)

# Visualizzare il DataFrame iniziale.
print("DATAFRAME ORIGINALE")
print(df)


# 2. Aggiungere la colonna "Totale Vendite".
# Moltiplicare la quantità per il prezzo unitario di ogni riga.
# Il risultato viene inserito in una nuova colonna.
df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]

# Visualizzare il DataFrame aggiornato con la nuova colonna.
print("DATAFRAME CON TOTALE VENDITE")
print(df)


# 3. Calcolare il totale delle vendite per ciascun prodotto.
# groupby("Prodotto") raggruppa le righe con lo stesso prodotto.
# ["Totale Vendite"] seleziona la colonna da analizzare.
# sum() somma i valori di ogni gruppo.
vendite_per_prodotto = df.groupby("Prodotto")["Totale Vendite"].sum()

# Visualizzare il totale delle vendite per prodotto.
print("TOTALE VENDITE PER PRODOTTO")
print(vendite_per_prodotto)


# 4. Trovare il prodotto più venduto in termini di quantità.
# Raggruppare le righe per prodotto e sommare le quantità vendute.
quantita_per_prodotto = df.groupby("Prodotto")["Quantità"].sum()

# idxmax() restituisce il nome del prodotto associato alla quantità massima.
prodotto_piu_venduto = quantita_per_prodotto.idxmax()

# max() restituisce il numero massimo di unità vendute.
quantita_massima = quantita_per_prodotto.max()

# Visualizzare il prodotto più venduto e la quantità totale.
print("PRODOTTO PIÙ VENDUTO")
print("Prodotto:", prodotto_piu_venduto)
print("Quantità venduta:", quantita_massima)


# 5. Identificare la città con il maggior volume di vendite.
# Raggruppare le righe per città e sommare i totali delle vendite.
vendite_per_citta = df.groupby("Città")["Totale Vendite"].sum()

# idxmax() restituisce la città con il totale più alto.
citta_migliore = vendite_per_citta.idxmax()

# max() restituisce il valore totale più alto tra le città.
totale_migliore = vendite_per_citta.max()

# Visualizzare la città con il maggior volume di vendite e il relativo totale.
print("CITTÀ CON IL MAGGIOR VOLUME DI VENDITE")
print("Città:", citta_migliore)
print("Totale vendite:", totale_migliore, "euro")


# 6. Creare un nuovo DataFrame con le vendite superiori a 1000 euro.
# La condizione controlla quali righe hanno un totale maggiore di 1000.
# Vengono mantenute soltanto le righe che soddisfano la condizione.
df_filtrato = df[df["Totale Vendite"] > 1000]

# Visualizzare il DataFrame contenente soltanto le vendite selezionate.
print("VENDITE SUPERIORI A 1000 EURO")
print(df_filtrato)


# 7. Ordinare il DataFrame per totale vendite in ordine decrescente.
# sort_values() ordina le righe in base alla colonna indicata da by.
# ascending=False ordina dal valore più alto al valore più basso.
# Il risultato viene assegnato nuovamente a df per conservarne l'ordine.
df = df.sort_values(by="Totale Vendite", ascending=False)

# Visualizzare il DataFrame ordinato.
print("DATAFRAME ORDINATO PER TOTALE VENDITE")
print(df)


# 8. Contare il numero di registrazioni di vendita per ogni città.
# value_counts() conta quante volte compare ciascuna città nella colonna.
numero_vendite_citta = df["Città"].value_counts()

# Visualizzare il numero di registrazioni per città.
print("NUMERO DI VENDITE PER CITTÀ")
print(numero_vendite_citta)
