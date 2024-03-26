class Personagem: 
    def __init__(self, nome, especie, forca_base):
        self._nome = nome
        self._especie = especie
        self._forca_base = forca_base

    @property 
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        raise ValueError("Você não pode alterar seu nome desta maneira.\n"
                         "O nome só pode ser modificada por métodos específicos.\n")
    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, nova_especie):
        self._especie = nova_especie
        raise ValueError("Você não pode alterar sua especie desta maneira.\n"
                         "A especie deve ser motificada utilizando o método específico\n")
    @property
    def forca_base(self): 
        return self._forca_base

    @forca_base.setter
    def forca_base(self, nova_forca_base):
        self._forca_base = nova_forca_base
        raise ValueError("Voce não deve alterar sua força desta maneira.\n"
                         "A força deve ser modificada utilizando o metodo especificado.\n")

    def calcular_forca(self): 
        return self._forca_base

    def __str__(self):
        return f"Nome do personagem é : {self._nome}, da especie {self._especie} com a força de: {self.calcular_forca():.3f}"

class Guerreiro(Personagem):
    def __init__(self, nome, especie, forca_base, espada, escudo):
        super().__init__(nome, especie, forca_base)
        self._forca = 45
        self.espada = espada
        self.escudo = escudo

    def calcular_forca(self):
        return super().calcular_forca() + self._forca

    def __str__(self):
        return f"Guerreiro - {super().__str__()}, Armas: {self.espada} e {self.escudo}"

class Mago(Personagem):
    def __init__(self, nome, especie, forca_base, cajado, livro):
        super().__init__(nome, especie, forca_base)
        self._forca = 10
        self.cajado = cajado
        self.livro = livro

    def calcular_forca(self):
        return super().calcular_forca() + self._forca

    def __str__(self):
        return f"Mago - {super().__str__()}, Armas: {self.cajado} e {self.livro}"

class Ladino(Personagem):
    def __init__(self, nome, especie, forca_base, adaga, funda):
        super().__init__(nome, especie, forca_base)
        self._forca = 25
        self.adaga = adaga
        self.funda = funda

    def calcular_forca(self):
        return super().calcular_forca() + self._forca

    def __str__(self):
        return f"Ladino - {super().__str__()}, Armas: {self.adaga} e {self.funda}"
