import mio_modulo as p

while True:
    print("MENU OPERAZIONI")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("0. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "0":
        print("Uscita dal programma.")
        break

    elif scelta in ["1", "2", "3", "4"]:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))

        if scelta == "1":
            risultato = p.somma(num1, num2)
            print("Risultato della somma:", risultato)

        elif scelta == "2":
            risultato = p.sottrazione(num1, num2)
            print("Risultato della sottrazione:", risultato)

        elif scelta == "3":
            risultato = p.moltiplicazione(num1, num2)
            print("Risultato della moltiplicazione:", risultato)

        elif scelta == "4":
            risultato = p.divisione(num1, num2)
            print("Risultato della divisione:", risultato)

    else:
        print("Opzione non valida, riprova!")