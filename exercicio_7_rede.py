class Perfil:
    def __init__(self, nome, nomedoperfil, seguidores):
        self.nome = nome
        self.nomedoperfil = nomedoperfil
        self.__seguidores = seguidores

    @property
    def seguidores(self):
        return self.__seguidores

    @seguidores.setter
    def seguidores(self):
        raise ValueError("Nao se pode alterar o valor desta forma")   

class Padrao(Perfil):
    def __init__(self, nome, nomedoperfil, seguidores, trabalho):
        super().__init__(nome, nomedoperfil, seguidores)
        self.trabalho = trabalho
        
class Influenciador(Perfil):
    def __init__(self, nome, nomedoperfil, seguidores, area):
        super().__init__(nome, nomedoperfil, seguidores)
        self.area = area
    
class Empresa(Perfil):
    def __init__(self, nome, nomedoperfil, seguidores, tipo):
        super().__init__(nome, nomedoperfil, seguidores)
        self.tipo = tipo
        