class Escola:
    def __init__(self,nome,codigo,ano):
        self.nome = nome
        self.__codigo = codigo
        self.__ano = ano

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def ano(self):
        return self.__ano
    
class Aluno(Escola):
    def __init__(self, nome, codigo, ano, idade):
        super().__init__(nome, codigo, ano)
        self.idade = idade

class Professor(Escola):
    def __init__(self, nome, codigo, ano, salario):
        super().__init__(nome, codigo, ano)
        self.__salario = salario
    def salario(self):
        return self.__salario
    
class Funcionario(Escola):
    def __init__(self, nome, codigo, ano, funcao):
        super().__init__(nome, codigo, ano)
        self.funcao = funcao
