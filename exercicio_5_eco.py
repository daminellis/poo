class SerVivo():
    def __init__(self, nome, especie, classe):
        self.nome = nome
        self.especie = especie
        self.__classe = classe

class Cachorro(SerVivo):
    def __init__(self, nome, especie, __classe, raca):
        super().__init__(nome, especie, __classe)
        self.raca = raca

class Humano(SerVivo):
    def __init__(self, nome, especie, __classe, sexo):
        super().__init__(nome, especie, __classe)
        self.sexo = sexo

class Planta(SerVivo):
    def __init__(self, nome, especie, __classe, pda):
        super().__init__(nome, especie, __classe)
        self.pda = pda

