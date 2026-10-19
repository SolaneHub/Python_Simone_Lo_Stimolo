nome = ""

while True:
    print("MENU File")
    print("1. Crea File")
    print("2. Modifica File")
    print("3. Leggi File")
    print("4. Svuota File")
    print("0. Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        nome = input("Che nome vuoi dare al file? ")
        file = open(nome, "w")
        file.close()
        print("File creato correttamente!")

    elif scelta == "2":
        if nome != "":
            file = open(nome, "a")
            frase = input("Scrivi cosa inserire nel file: ")
            file.write(frase + "\n")
            file.close()
        else:
            print("Devi prima creare un file!")

    elif scelta == "3":
        if nome != "":
            file = open(nome, "r")
            contenuto = file.read()
            file.close()
            print(contenuto)
        else:
            print("Devi prima creare un file!")

    elif scelta == "4":
        if nome != "":
            file = open(nome, "w")
            file.close()
            print("File svuotato correttamente!")
        else:
            print("Devi prima creare un file!")

    elif scelta == "0":
        break

    else:
        print("Scelta non valida!")