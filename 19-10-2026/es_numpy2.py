import numpy as np

# 1. Crea un array 1D con 20 numeri casuali tra 10 e 50
arr1 = np.random.randint(10, 50, size=20)

# 2. Estrai i primi 10 elementi
primi_10 = arr1[:10].copy()

# 3. Estrai gli ultimi 5 elementi
ultimi_5 = arr1[-5:].copy()

# 4. Estrai gli elementi dall'indice 5 all'indice 15 (escluso)
elementi_5_15 = arr1[5:15].copy()

# 5. Estrai ogni terzo elemento
ogni_terzo = arr1[::3].copy()

# 6. Modifica gli elementi dall'indice 5 all'indice 10 (escluso)
arr1[5:10] = 99

# 7. Stampa l'array e tutti i sottoarray
print("Array originale dopo la modifica:")
print(arr1)

print("Primi 10 elementi:")
print(primi_10)

print("Ultimi 5 elementi:")
print(ultimi_5)

print("Elementi dall'indice 5 al 14:")
print(elementi_5_15)

print("Ogni terzo elemento:")
print(ogni_terzo)
