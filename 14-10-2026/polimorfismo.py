class MetodoPagamento:
    def effettua_pagamento(self, importo):
        return f"Hai effettuato un pagamento di {importo}€"


class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        return super().effettua_pagamento(importo) + " tramite Carta di Credito"


class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        return super().effettua_pagamento(importo) + " tramite PayPal"


class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        return super().effettua_pagamento(importo) + " tramite Bonifico Bancario"


class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento

    def transazione(self, importo):
        return self.metodo_pagamento.effettua_pagamento(importo)


transazione_cdc = GestorePagamenti(CartaDiCredito())
transazione_pp = GestorePagamenti(PayPal())
transazione_bb = GestorePagamenti(BonificoBancario())

print(transazione_cdc.transazione(100))
print(transazione_pp.transazione(500))
print(transazione_bb.transazione(11000))
