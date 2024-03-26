from exercicio_12_mercado import Acao,Fundo,Titulo

acao = Acao("Empresa X", 1000, 50, 20)
titulo = Titulo("Título do Governo", 5000, 0.03, 2)
fundo = Fundo("FII Y", 2000, 100, 25)

print("Retorno da Ação:", acao.calcular_retorno())
print("Risco da Ação:", acao.calcular_risco())

print("Retorno do Título:", titulo.calcular_retorno())
print("Risco do Título:", titulo.calcular_risco())

print("Retorno do Fundo Imobiliário:", Fundo.calcular_retorno())
print("Risco do Fundo Imobiliário:", Fundo.calcular_risco())
