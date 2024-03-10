from modelos.avaliação import Avaliacao
from modelos.cardapio.cardapio import ItemCardapio


class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'   {self.nome.ljust(20)} | {self.categoria.ljust(20)} | {self.ativo}'
    
    @classmethod
    def lista_restaurantes(cls):

        print(f'   {'nome do restaurante'.ljust(20)} | {'categoria'.ljust(20)} | {'avaliaçao⭐'. ljust(10)} | status ')
        print('   ---------------------+----------------------+-------------+------------------')
        for restaurante in cls.restaurantes:
            print(f'   {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(f'{restaurante.media_avaliacao}⭐').center(10)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'aberto' if self._ativo else 'fechado'
    
    def altera_estado(self):
        self._ativo = not self._ativo

    def recebe_avaliacao(self, cliente , nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_de_notas = len(self._avaliacao)

        media = round(soma_das_notas / qtd_de_notas, 1)
        return media

    #def adiciona_bebida(self, bebida):
    #    self._cardapio.append(bebida)

    #def adiciona_prato(self, prato):
    #    self._cardapio.append(prato)

    def adiciona_no_cardapio(self, item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f'cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio,start=1):

            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | preço: R${item._preco} | decrição: {item._descricao}'
                print(mensagem_prato)

            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | preço: R${item._preco} | tamanho: {item._ml}'
                print(mensagem_bebida)