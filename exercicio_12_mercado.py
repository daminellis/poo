import random

class Investimento:
    def __init__(self, nome, valor_investido):
        self.nome = nome
        self.valor_investido = valor_investido
    
    def calcular_retorno(self):
        pass
    
    def calcular_risco(self):
        pass

class Acao(Investimento):
    def __init__(self, nome, valor_investido, preco_atual, quantidade):
        super().__init__(nome, valor_investido)
        self.preco_atual = preco_atual
        self.quantidade = quantidade
    
    def calcular_retorno(self):
        return (self.preco_atual * self.quantidade - self.valor_investido) / self.valor_investido
    
    def calcular_risco(self):
        return random.uniform(0.05, 0.15) #calculo de risco

class Titulo(Investimento):
    def __init__(self, nome, valor_investido, taxa_juros, periodo):
        super().__init__(nome, valor_investido)
        self.taxa_juros = taxa_juros
        self.periodo = periodo
    
    def calcular_retorno(self):
        return self.valor_investido * self.taxa_juros * self.periodo
    
    def calcular_risco(self):
        return random.uniform(0.01, 0.05)  #outro calc de risco 

class Fundo(Investimento):
    def __init__(self, nome, valor_investido, cotas, valor_cota_atual):
        super().__init__(nome, valor_investido)
        self.cotas = cotas
        self.valor_cota_atual = valor_cota_atual
    
    def calcular_retorno(self):
        return (self.cotas * self.valor_cota_atual - self.valor_investido) / self.valor_investido
    
    def calcular_risco(self):
        return random.uniform(0.03, 0.1)  #mais um é isso ai 

