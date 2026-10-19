import numpy as np

# 1. Crea una matrice 6x6 con numeri casuali da 1 a 100
a = np.random.randint(1, 101, size=(6, 6))

# 2. Estrai la sotto-matrice centrale 4x4
sm = a[1:5, 1:5].copy()

# 3. Inverti le righe della sotto-matrice
iv = sm[::-1, :].copy()

# 4. Estrai la diagonale principale
dg = iv.diagonal().copy()

# 5. Sostituisci i multipli di 3 con -1
md = iv.copy()
md[md % 3 == 0] = -1

# 6. Stampa i risultati
print("Matrice originale:")
print(a)

print("\nSottomatrice centrale 4x4:")
print(sm)

print("\nMatrice invertita:")
print(iv)

print("\nDiagonale principale:")
print(dg)

print("\nMatrice modificata:")
print(md)