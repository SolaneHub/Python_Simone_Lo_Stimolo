import random


def inserimento():
  notPositive = True
  while notPositive:
    n = int(input("Inserisci un numero\n> "))
    if n > 0:
      notPositive = False
  return n

num = inserimento()

def generatore(num):
  lista = []
  for i in range(num):
    lista.append(random.randint(1, 100)) 
  lista.sort()
  return lista

lista = generatore(num)

def sommaPari(lista):
  sommaPari = 0
  
  for i in lista:
    if i % 2 == 0:
      sommaPari += i
      
  return sommaPari


print("Somma Pari\n >", sommaPari(lista))  

def listaDispari(lista):
  listaDispari = []
  for i in lista:
    if i % 2 == 1:
      listaDispari.append(i)
      
  return listaDispari

print("Lista Dispari\n >", listaDispari(lista)) 

def isPrimo(num):
  if num < 2:
      return False
    
  for i in range(2, num):
      if num % i == 0:
        return False
    
  return True
  
  
num = int(input("Inserisci un numero\n> "))

print(isPrimo(num))

def listaPrimi(lista):
    for i in lista:
        if isPrimo(i):
            print(">", i, "é primo")
      
listaPrimi(lista)


def isSommaListaPrimi(lista):

    sommaTotale = 0

    for i in lista:
        sommaTotale += i

    if isPrimo(sommaTotale):
        print("La somma è un primo", sommaTotale)
        
isSommaListaPrimi(lista)
    

print("Lista completa\n> ", lista)  