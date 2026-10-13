class Convertitore:
  @staticmethod
  def euro_in_dollari(euro):
    return euro * 1.08
  
  @staticmethod
  def km_in_miglia(km):
    return km * 0.621371
  
  
dollari = Convertitore.euro_in_dollari(300)
print(dollari)
miglia = Convertitore.km_in_miglia(150)
print(miglia)
