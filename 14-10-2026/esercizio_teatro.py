
while True:
    class Posto:
        def __init__(self, numero, fila):
            self.__numero = numero
            self.__fila = fila
            self.__occupato = False

        def get_numero(self):
            return self.__numero

        def get_fila(self):
            return self.__fila

        def get_occupato(self):
            return self.__occupato

        def prenota(self):
            if not self.__occupato:
                self.__occupato = True
                print("Posto prenotato con successo!")
            else:
                print("Il posto è già occupato.")

        def libera(self):
            if self.__occupato:
                self.__occupato = False
                print("Posto liberato!")
            else:
                print("Il posto non era prenotato.")


    class PostoVIP(Posto):
        def __init__(self, numero, fila):
            super().__init__(numero, fila)
            self.__servizi_extra = ["Lounge VIP", "Buffet"]

        def prenota(self):
            if not self.get_occupato():
                super().prenota()
                print(f"Servizi aggiuntivi: {self.__servizi_extra}")
            else:
                super().prenota()


    class PostoStandard(Posto):
        def __init__(self, numero, fila):
            super().__init__(numero, fila)
            self.__costo = 30


    class Teatro:
        def __init__(self):
            self._posti = []

        def aggiungi_posto(self, posto):
            self._posti.append(posto)

        def prenota_posto(self, numero, fila):
            for posto in self._posti:
                if posto.get_numero() == numero and posto.get_fila() == fila:
                    posto.prenota()
                    return

            print("Posto non trovato.")

        def stampa_posti_occupati(self):
            for posto in self._posti:
                if posto.get_occupato():
                    print(f"Fila {posto.get_fila()}, posto {posto.get_numero()}")


    teatro = Teatro()

    vip = PostoVIP(1, "A")
    standard = PostoStandard(2, "B")

    teatro.aggiungi_posto(vip)
    teatro.aggiungi_posto(standard)

    print("MENU TEATRO")
    print("1. Prenota posto VIP")
    print("2. Prenota posto Standard")
    print("3. Visualizza posti occupati")
    print("4. Libera posto VIP")
    print("5. Libera posto Standard")
    print("0. Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        teatro.prenota_posto(1, "A")
    elif scelta == "2":
        teatro.prenota_posto(2, "B")
    elif scelta == "3":
        teatro.stampa_posti_occupati()
    elif scelta == "4":
        vip.libera()
    elif scelta == "5":
        standard.libera()
    elif scelta == "0":
        print("Arrivederci!")
        break
    else:
        print("Scelta non valida.")
