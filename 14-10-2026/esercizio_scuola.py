class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_eta(self):
        return self.__eta

    def set_eta(self, eta):
        self.__eta = eta

    def presentazione(self):
        return f"{self.__nome} {self.__eta}"


class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        self.__voti = voti

    def calcola_media(self):
        tot = 0
        for v in self.__voti:
            tot += v

        return tot / len(self.__voti)

    def presentazione(self):
        return f"{super().presentazione()} Media: {self.calcola_media()}"


class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia

    def presentazione(self):
        return f"{super().presentazione()} Materia: {self.__materia}"


class Scuola:
    def __init__(self, nome):
        self.__nome = nome
        self.__persone = {"studenti": [], "professori": []}

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_studenti(self):
        return self.__persone["studenti"]

    def set_studente(self, studente):
        self.__persone["studenti"].append(studente)

    def get_professori(self):
        return self.__persone["professori"]

    def set_professore(self, professore):
        self.__persone["professori"].append(professore)


scuola_1 = Scuola("Istituto Ferraris")

studente_1 = Studente("Piero", 20, [10, 5, 6, 8, 4, 3])

professore_1 = Professore("Gianni", 43, "Geografia")

scuola_1.set_studente(studente_1)
scuola_1.set_professore(professore_1)

print(scuola_1.get_nome())

for studente in scuola_1.get_studenti():
    print(studente.presentazione())
    
for professore in scuola_1.get_professori():
    print(professore.presentazione())