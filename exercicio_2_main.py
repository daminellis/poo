from exercicio_2_banco import ContaCorrente, ContaPP

corrente = ContaCorrente("Joao", "joao1234", "joao@gmail.com", 1234, 1000)
#print(corrente.__dict__)

#corrente.chequeEspecial()
#corrente.sacar(100)
#corrente.depositar(100)

pp = ContaPP("Joao", "joao1234", "joao@gmail.com", 1234, 1000)
print(pp.__dict__)
pp.calcularJuros()
print(pp.__dict__)