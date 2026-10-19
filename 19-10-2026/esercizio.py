import numpy as np

# Creazione di un array unidimensionale

arr = np.array([1, 2, 3, 4, 5])


# Creazione di un array bidimensionale

arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Utilizzo di alcuni metodi

print("Forma dell'array:", arr.shape)  # Output: (5,)

print("Dimensioni dell'array:", arr.ndim)  # Output: 1

print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)

print("Numero di elementi:", arr.size)  # Output: 5

print("Somma degli elementi:", arr.sum())  # Output: 15

print("Media degli elementi:", arr.mean())  # Output: 3.0

print("Valore massimo:", arr.max())  # Output: 5

print("Indice del valore massimo:", arr.argmax())  # Output: 4

arr = np.array([1, 2, 3], dtype='int32')

print(arr.dtype)  # Output: int32

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # Output: (2, 3)

arr = np.arange(10)

print(arr)  # Output: [0 1 2 3 4 5 6 7 8 9]

arr = np.arange(6)

reshaped_arr = arr.reshape((2, 3))

print(reshaped_arr)

# Output:  [[0 1 2] [3 4 5]]