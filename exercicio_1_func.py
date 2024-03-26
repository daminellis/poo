class Funcionario:
    def __init__(self, nome, salario_base):
        self._nome = nome  
        self._salario_base = salario_base  
    
    @property
    def nome(self):
        return self._nome

    @property
    def salario_base(self):
        return self._salario_base

    def calcular_salario(self):
        return self._salario_base 
    
    def __str__(self):
        return f"Nome: {self._nome}, Salário: R${self.calcular_salario():.2f}"  

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.__bonus = bonus  
    
    def calcular_salario(self):
        return super().calcular_salario() + self.__bonus  
    
    def __str__(self):
        return f"Gerente - {super().__str__()}, Bônus: R${self.__bonus:.2f}"  


class Programador(Funcionario):
    def __init__(self, nome, salario_base, linguagem, horas_extra):
        super().__init__(nome, salario_base)
        self.__linguagem = linguagem 
        self.__horas_extra = horas_extra  
    
    def calcular_salario(self):
        return super().calcular_salario() + self.__horas_extra * 20  
    
    def __str__(self):
        return f"Programador - {super().__str__()}, Linguagem: {self.__linguagem}, Horas Extras: {self.__horas_extra}"


class Analista(Funcionario):
    def __init__(self, nome, salario_base, nivel):
        super().__init__(nome, salario_base)
        self.__nivel = nivel  
    
    def calcular_salario(self):
        if self.__nivel == "junior":
            return super().calcular_salario() + 2000
        elif self.__nivel == "pleno":
            return super().calcular_salario() + 3000
        elif self.__nivel == "senior":
            return super().calcular_salario() + 5000
        else:
            return super().calcular_salario()
    
    def __str__(self):
        return f"Analista - {super().__str__()}, Nível: {self.__nivel}"
