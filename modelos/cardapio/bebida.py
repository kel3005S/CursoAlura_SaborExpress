from modelos.cardapio.cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, ml):
        super().__init__(nome, preco)
        self._ml = ml

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)