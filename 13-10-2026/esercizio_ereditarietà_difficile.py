class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"{self.nome} avanza")

    def attacca(self):
        print(f"{self.nome} attacca")

    def ritira(self):
        print(f"{self.nome} si ritira")


class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        return super().muovi()

    def attacca(self):
        return super().attacca()

    def ritira(self):
        return super().ritira()

    def costruisci_trincea(self):
        print(f"{self.nome} costruisce una trincea.")


class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        return super().muovi()

    def attacca(self):
        return super().attacca()

    def ritira(self):
        return super().ritira()

    def calibra_artiglieria(self):
        print(f"{self.nome} calibra artiglieria.")


class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        return super().muovi()

    def attacca(self):
        return super().attacca()

    def ritira(self):
        return super().ritira()

    def esplora_terreno(self):
        print(f"{self.nome} sta esplorando.")


class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        return super().muovi()

    def attacca(self):
        return super().attacca()

    def ritira(self):
        return super().ritira()

    def rifornisci_unita(self):
        print(f"{self.nome} sta rifornendo.")


class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        return super().muovi()

    def attacca(self):
        return super().attacca()

    def ritira(self):
        return super().ritira()

    def conduci_ricognizione(self):
        print(f"{self.nome} sta sorvegliando.")


class ControlloMilitare(
    Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione
):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.unita_registrate = {
            "Fanteria": [],
            "Artiglieria": [],
            "Cavalleria": [],
            "SupportoLogistico": [],
            "Ricognizione": [],
        }

    def registra_unita(self, unita):
        if unita.nome == "Fanteria":
            self.unita_registrate["Fanteria"].append(unita)
        elif unita.nome == "Artiglieria":
            self.unita_registrate["Artiglieria"].append(unita)
        elif unita.nome == "Cavalleria":
            self.unita_registrate["Cavalleria"].append(unita)
        elif unita.nome == "SupportoLogistico":
            self.unita_registrate["SupportoLogistico"].append(unita)
        elif unita.nome == "Ricognizione":
            self.unita_registrate["Ricognizione"].append(unita)

        print(f"Unità {unita.nome} registrata")

    def mostra_unita(self):
        for tipo in self.unita_registrate:
            print(f"{tipo}:")
            for unita in self.unita_registrate[tipo]:
                print(f"  Nome: {unita.nome}")
                print(f"  Numero soldati: {unita.numero_soldati}")

    def dettagli_unita(self, nome):
        for tipo in self.unita_registrate:
            for unita in self.unita_registrate[tipo]:
                if unita.nome == nome:
                    print(f"Nome: {unita.nome}")
                    print(f"Numero soldati: {unita.numero_soldati}")


controllo = ControlloMilitare("Comando Centrale", 0)

fanteria_1 = Fanteria("Fanteria", 100)
artiglieria_1 = Artiglieria("Artiglieria", 50)
cavalleria_1 = Cavalleria("Cavalleria", 75)
supporto_1 = SupportoLogistico("SupportoLogistico", 30)
ricognizione_1 = Ricognizione("Ricognizione", 20)

controllo.registra_unita(fanteria_1)
controllo.registra_unita(artiglieria_1)
controllo.registra_unita(cavalleria_1)
controllo.registra_unita(supporto_1)
controllo.registra_unita(ricognizione_1)

print("Unità registrate:")
controllo.mostra_unita()

fanteria_1.costruisci_trincea()
artiglieria_1.calibra_artiglieria()
cavalleria_1.esplora_terreno()
supporto_1.rifornisci_unita()
ricognizione_1.conduci_ricognizione()
