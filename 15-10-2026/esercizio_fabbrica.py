class Pezzo:
    def __init__(self, nome, quantita):
        self.__nome = nome
        self.__quantita = quantita

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_quantita(self):
        return self.__quantita

    def set_quantita(self, quantita):
        self.__quantita = quantita


class Fabbrica:
    def __init__(self):
        self.produzione = {}


fabbrica = Fabbrica()

while True:
    print("MENU Fabbrica")
    print("1. Aggiungi Prodotto")
    print("2. Visualizza Produzione")
    print("3. Cerca Prodotto")
    print("4. Modifica Quantità")
    print("5. Rimuovi Prodotto")
    print("6. Calcola Totale Pezzi Prodotti")
    print("0. Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        nome = input("Inserisci nome prodotto: ")
        quantita = int(input("Inserisci la quantità: "))

        pezzo = Pezzo(nome, quantita)
        fabbrica.produzione[nome] = pezzo

    elif scelta == "2":
        print("Elenco produzione:\n")
        for nome, pezzo in fabbrica.produzione.items():
            print(f"Nome: {nome}")
            print(f"Quantità: {pezzo.get_quantita()}")

    elif scelta == "3":
        nome = input("Quale pezzo vuoi cercare? ")
        if nome in fabbrica.produzione:
            pezzo = fabbrica.produzione[nome]
            print(f"Quantità: {pezzo.get_quantita()}")
        else:
            print("Pezzo non trovato.")

    elif scelta == "4":
        nome = input("Quale pezzo vuoi modificare? ")
        if nome in fabbrica.produzione:
            quantita = int(input("Qual è la nuova quantità?"))
            pezzo.set_quantita(quantita)
            print(f"Quantità aggiornata: {pezzo.get_quantita()}")
        else:
            print("Pezzo non trovato.")

    elif scelta == "5":
        nome = input("Quale pezzo vuoi eliminare? ")
        if nome in fabbrica.produzione:
            del fabbrica.produzione[nome]
            print("Prodotto rimosso!")
        else:
            print("Prodotto non trovato.")

    elif scelta == "6":
        tot = 0
        for pezzo in fabbrica.produzione.values():
            tot =+ pezzo.get_quantita()
        print(f"Il totale dei pezzi prodotti è: {tot}")

    elif scelta == "0":
        break
