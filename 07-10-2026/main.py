while True:
    esercizio = input("Che esercizio vuoi fare?\n> ")

    match esercizio:
        case "while":
            # ==============================================================
            # ESERCIZIO 1: WHILE
            # ==============================================================

            tot = 0
            num = int(input("Inserisci un numero\n> "))

            while num != 0:
                tot += num
                num = int(input("Inserisci un numero\n> "))

            print("La somma di tutti i numeri è: ", tot)

        case "for":
            # ==============================================================
            # ESERCIZIO 2: FOR
            # ==============================================================

            parola = input("Inserisci una parola\n> ")

            for lett in parola:
                print(lett)

        case "forrange":
            # ==============================================================
            # ESERCIZIO 3: FOR RANGE
            # ==============================================================
            massimo = int(input("Inserisci il numero massimo\n> "))
            steps = int(input("Inserisci i salti tra i numeri\n> "))

            for i in range(0, massimo, steps):
                print(i)