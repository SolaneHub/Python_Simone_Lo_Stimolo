n = int(input("Inserisci un numero\n> "))

while n <= 0:
    n = int(input("Inserisci un numero\n> "))

pari = 0
dispari = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        pari += i
    else:
        dispari += i

print("Somma pari:", pari)
print("Somma dispari:", dispari)

if n < 2:
    primo = False
else:
    primo = True

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

if primo:
    print(n, "è primo")
else:
    print(n, "non è primo")