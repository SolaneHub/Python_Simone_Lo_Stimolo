class Animale:
    nome =""
    eta = 0
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
  
    def fai_suono(self):
        print(f"{self.nome} fa suono generico.")
        
class Leone(Animale):
  
  def __init__(self, nome, eta):
     super().__init__(nome, eta)
  
  def caccia(self):
    print(f"{self.nome} sta cacciando")
    
    
  def fai_suono(self):
      print(f"{self.nome} sta ruggendo")

  
class Giraffa(Animale):
    def __init__(self, nome, eta):
     super().__init__(nome, eta)
     
     def 
     
     
    def fai_suono(self):
      print(f"{self.nome} landita")

class Pinguino(Animale):