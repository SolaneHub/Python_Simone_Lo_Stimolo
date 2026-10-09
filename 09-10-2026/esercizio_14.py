nome_registrato = ""
codice_registrato = ""

risultati = []

while True:
    print("MENU PRINCIPALE")
    print("1. Registrazione")
    print("2. Login")
    print("0. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "0":
        break

    elif scelta == "1":
        nome = input("Inserisci il nome: ")

        while nome == "":
            nome = input("Il nome è obbligatorio. Inseriscilo: ")

        codice = input("Inserisci un codice: ")

        while codice == "":
            codice = input("Il codice è obbligatorio. Inseriscilo: ")

        nome_registrato = nome
        codice_registrato = codice

        print("Registrazione completata!")

    elif scelta == "2":
        if nome_registrato == "" or codice_registrato == "":
            print("Devi registrarti prima di effettuare il login.")

        else:
            nome_login = input("Inserisci il nome: ")
            codice_login = input("Inserisci il codice: ")

            if nome_login == nome_registrato and codice_login == codice_registrato:
                print("Login effettuato!")

                while True:
                    print("MENU OPERAZIONI")
                    print("1. Somma")
                    print("2. Sottrazione")
                    print("3. Visualizza risultati")
                    print("0. Logout")

                    scelta_operazione = input("Scegli un'opzione: ")

                    if scelta_operazione == "0":
                        break

                    elif scelta_operazione == "1":
                        numero1 = int(input("Inserisci il primo numero: "))
                        numero2 = int(input("Inserisci il secondo numero: "))

                        risultato = numero1 + numero2

                        print("Risultato:", risultato)

                        risultati.append(
                            "Somma: "
                            + str(numero1)
                            + " + "
                            + str(numero2)
                            + " = "
                            + str(risultato)
                        )

                    elif scelta_operazione == "2":
                        numero1 = int(input("Inserisci il primo numero: "))
                        numero2 = int(input("Inserisci il secondo numero: "))

                        risultato = numero1 - numero2

                        print("Risultato:", risultato)

                        risultati.append(
                            "Sottrazione: "
                            + str(numero1)
                            + " - "
                            + str(numero2)
                            + " = "
                            + str(risultato)
                        )

                    elif scelta_operazione == "3":
                        if len(risultati) == 0:
                            print("Non ci sono risultati salvati.")

                        else:
                            print("RISULTATI SALVATI")

                            for operazione in risultati:
                                print(operazione)

                    else:
                        print("Scelta non valida.")

            else:
                print("Nome o codice errato.")

    else:
        print("Scelta non valida.")

print("Programma terminato.")
