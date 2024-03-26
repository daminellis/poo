  class Venda():
    def __init__(self, nome, tipo, preco):
        self.nome = nome
        self.tipo = tipo
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self):
        raise ValueError("Nao pode alterar o valor do saldo por este caminho!")

class Eletronicos(Venda):
    def __init__(self, nome, tipo, preco, marca):
        super().__init__(nome, tipo, preco)
        self.marca = marca

    
class Vestuario(Venda):
    def __init__ (self, nome, tipo, preco, cor):
        super().__init__(nome, tipo, preco)
        self.cor = cor

class Alimento(Venda):
    def __init__ (self, nome, tipo, preco, fruta):
        super().__init__(nome, tipo, preco)
        self.fruta = fruta
