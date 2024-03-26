class Conta():
    def __init__(self, nome, senha, email, cpf, saldo):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.cpf = cpf
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
        
    @saldo.setter
    def saldo(self):
        raise ValueError("Nao pode alterar o valor do saldo!")

    def sacar(self, a):
        if a < self.__saldo:
            self.__saldo -= a
            print("seu saldo atual é de: ", self.__saldo)
        else:
            print("O Valor solicitado nao pode ser sacado")

    def depositar(self, a):
        self.__saldo += a
        print("seu saldo atual é de: ", self.__saldo)


class ContaCorrente(Conta):
    def __init__(self, nome, senha, email, cpf,saldo):
        super().__init__(nome, senha, email, cpf,saldo)
        self.__credito = 0

    def chequeEspecial(self):
        resposta = input("Voce deseja soliciar um crédito? S/N")

        if resposta.upper() == 'S':
            novoValorCredito = int(input("Digite o novo valor:"))
            self.__credito += novoValorCredito
        else:
            return

class ContaPP(Conta):
    def __init__(self, nome, senha, email, cpf, saldo):
        super().__init__(nome, senha, email, cpf, saldo)
        
    def calcularJuros(self):
        dias = int(input("Digite a quantidade de dias que voce deseja calcular: "))
        porcent = 0.1
        if dias > 31:
            print("Digite o dia novamente.")
            dias = int(input("Digite a quantidade de dias que voce deseja calcular: "))
        else:
            valorJuros = porcent * dias
            self.depositar(valorJuros)
            print("Valor do saldo com juros: ", self.saldo)
