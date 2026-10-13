class Animale:
  numero_animali = 0
  
  def __init__(self, nome, specie):
    self.nome = nome
    self.specie = specie
    Animale.numero_animali += 1
    
  @classmethod
  def quanti_animali(cls):
    print(f"Numero di animali creati: {cls.numero_animali}")
    
    
animale1 = Animale("Luna", "Gatto")
animale2 = Animale("Fido", "Cane")
animale3 = Animale("Bunny", "Coniglio")

Animale.quanti_animali()