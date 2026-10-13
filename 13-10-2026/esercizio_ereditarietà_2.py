class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

    def stampa_info(self):
        print(f"Nome: {self.nome}")
        print(f"Costo di produzione: {self.costo_produzione} €")
        print(f"Prezzo di vendita: {self.prezzo_vendita} €")
        print(f"Profitto: {self.calcola_profitto()} €")


class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia

    def stampa_info(self):
        print("--- Prodotto elettronico ---")
        super().stampa_info()
        print(f"Garanzia: {self.garanzia}")


class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

    def stampa_info(self):
        print("--- Prodotto di abbigliamento ---")
        super().stampa_info()
        print(f"Materiale: {self.materiale}")


prodotto = Prodotto("Sedia", 30, 60)
televisore = Elettronica("Televisore", 250, 400, "2 anni")
maglietta = Abbigliamento("Maglietta", 8, 25, "Cotone")

prodotto.stampa_info()
televisore.stampa_info()
maglietta.stampa_info()


class Fabbrica:
    def __init__(self):
        self.nome_prod = []
        self.num_prod = []

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.nome_prod:
            indice = self.nome_prod.index(prodotto.nome)
            self.num_prod[indice] += quantita
        else:
            self.nome_prod.append(prodotto.nome)
            self.num_prod.append(quantita)

    def vendi_prodotto(self, prodotto, quantita):
        if prodotto.nome not in self.nome_prod:
            print("Prodotto non presente in inventario.")
            return

        indice = self.nome_prod.index(prodotto.nome)

        if self.num_prod[indice] < quantita:
            print("Quantità insufficiente in magazzino.")
            return

        self.num_prod[indice] -= quantita

        profitto = prodotto.calcola_profitto() * quantita
        print(f"Profitto della vendita: {profitto} €")

    def resi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.nome_prod:
            indice = self.nome_prod.index(prodotto.nome)
            self.num_prod[indice] += quantita
        else:
            self.nome_prod.append(prodotto.nome)
            self.num_prod.append(quantita)

fabbrica = Fabbrica()

fabbrica.aggiungi_prodotto(televisore, 5)
fabbrica.aggiungi_prodotto(maglietta, 10)

print("Inventario iniziale:")
print(fabbrica.nome_prod)
print(fabbrica.num_prod)


fabbrica.vendi_prodotto(televisore, 2)

fabbrica.resi_prodotto(televisore, 1)

print("Inventario finale:")
print(fabbrica.nome_prod)
print(fabbrica.num_prod)