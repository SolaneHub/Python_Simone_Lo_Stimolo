import random

randInt = random.randint(1, 100)

def indovina(randInt):
  not_Found = True
  while not_Found:
    inputInt = int(input("Inserisci un numero\n>"))
    if inputInt == randInt:
      print("Hai trovato il numero"),
      not_Found = False
    elif inputInt > randInt:
      print("Il numero è più piccolo")
    elif inputInt < randInt:
      print("Il numero è più grande")  

indovina(randInt)


def fibonacci(inputInt):
    a = 0
    b = 1

    for i in range(inputInt + 1):
        if a > inputInt:
            break
        print(a)
        
        temp = a
        a = b
        b = temp + b

inputInt = int(input("Inserisci un numero per la sequenza di Fibonacci\n> "))

fibonacci(inputInt)