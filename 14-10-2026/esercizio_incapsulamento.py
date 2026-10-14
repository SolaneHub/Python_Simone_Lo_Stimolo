class ContoBancario:
    def __init__(self, titolare, saldo):
        self.__titolare = titolare
        self.__saldo = saldo

    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, titolare):
        self.__titolare = titolare

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Hai depositato: {importo}€")
        else:
            print("L'importo deve essere positivo")

    def preleva(self, importo):
        if importo > 0 and importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Hai prelevato: {importo}€")
        else:
            print("Importo non valido o saldo insufficiente.")

    def visualizza_saldo(self):
        print(f"Hai {self.__saldo}€ nel conto")


conto1 = ContoBancario("Gianni", 1000)

print(conto1.get_titolare())
print(conto1.get_saldo())

conto1.deposita(200)
conto1.preleva(50)
conto1.visualizza_saldo()
