lista_interi = []
lista_float = []
lista_stringhe = []
lista_booleani = []

while True:
    print("SCEGLI IL TIPO DI LISTA")
    print("1. Interi")
    print("2. Float")
    print("3. Stringhe")
    print("4. Booleani")
    print("0. Esci")

    scelta_tipo = input("Scelta: ")

    if scelta_tipo == "0":
        break

    elif scelta_tipo == "1":
        lista = lista_interi
        tipo = "int"

    elif scelta_tipo == "2":
        lista = lista_float
        tipo = "float"

    elif scelta_tipo == "3":
        lista = lista_stringhe
        tipo = "str"

    elif scelta_tipo == "4":
        lista = lista_booleani
        tipo = "bool"

    else:
        print("Scelta non valida")
        continue

    while True:
        print("MENU OPERAZIONI")
        print("1. Inserisci in fondo")
        print("2. Inserisci in una posizione")
        print("3. Modifica tutta la lista")
        print("4. Stampa la lista")
        print("5. Elimina tutta la lista")
        print("0. Torna alla scelta del tipo")

        scelta = input("Scelta: ")

        if scelta == "0":
            break

        elif scelta == "1" or scelta == "2":
            if tipo == "int":
                valore = int(input("Inserisci un intero: "))

            elif tipo == "float":
                valore = float(input("Inserisci un decimale: "))

            elif tipo == "str":
                valore = input("Inserisci un testo: ")

            elif tipo == "bool":
                valore = input("Inserisci True oppure False: ")

                if valore == "True":
                    valore = True
                else:
                    valore = False

            if scelta == "1":
                lista.append(valore)
                print("Elemento aggiunto in fondo")

            else:
                posizione = int(input("In quale posizione vuoi inserirlo? "))

                if posizione >= 0 and posizione <= len(lista):
                    lista.insert(posizione, valore)
                    print("Elemento inserito")
                else:
                    print("Posizione non valida")

        elif scelta == "3":
            lista.clear()

            numero = int(input("Quanti elementi vuoi inserire nella nuova lista? "))

            while numero < 0:
                numero = int(input("Inserisci un numero maggiore o uguale a zero: "))

            for i in range(numero):
                if tipo == "int":
                    valore = int(input("Inserisci un intero: "))

                elif tipo == "float":
                    valore = float(input("Inserisci un decimale: "))

                elif tipo == "str":
                    valore = input("Inserisci un testo: ")

                elif tipo == "bool":
                    valore = input("Inserisci True oppure False: ")

                    if valore == "True":
                        valore = True
                    else:
                        valore = False

                lista.append(valore)

            print("Lista modificata:", lista)

        elif scelta == "4":
            print("Contenuto della lista:", lista)

        elif scelta == "5":
            lista.clear()
            print("Lista svuotata")

        else:
            print("Scelta non valida")

print("Programma terminato")
