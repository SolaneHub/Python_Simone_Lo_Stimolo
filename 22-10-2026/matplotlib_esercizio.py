import random

import matplotlib.pyplot as plt
import pandas as pd

# inizializzo lista vuota per poter mettere temperature
temperature = []

# inserisco 30 temperature nella lista
for i in range(30):
    temp = random.randint(-5, 35)
    temperature.append(temp)

print(temperature)

# creo un dataframe con la lista temperature
df = pd.DataFrame({"temperature": temperature})

print(df)

# massimo e minimo presi dal dataframe
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()

print("Temperatura massima:", max_temp)
print("Temperatura minima:", min_temp)

# media e mediana
avg_temp = df["temperature"].mean()
med_temp = df["temperature"].median()

print("Temperatura media:", avg_temp)
print("Mediana delle temperature:", med_temp)

# creazione grafico istogramma
plt.hist(df["temperature"])
plt.title("Distribuzione delle temperature giornaliere")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Numero di giorni")

plt.show()
