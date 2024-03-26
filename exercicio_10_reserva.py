class Voo:
    def __init__(self, origem, destino, data, capacidade):
        self._origem = origem
        self._destino = destino
        self._data = data
        self._capacidade = capacidade
        self._assentos_ocupados = 0
    
    def calcular_preco(self):
        raise NotImplementedError("Método calcular_preco não implementado.")
    
    def verificar_disponibilidade(self):
        return self._capacidade - self._assentos_ocupados
    
    def reservar(self, quantidade):
        if quantidade <= self.verificar_disponibilidade():
            self._assentos_ocupados += quantidade
            print(f"{quantidade} assentos reservados com sucesso.")
        else:
            print("Não há assentos disponíveis para essa quantidade.")
    
    def __str__(self):
        return f"Voo de {self._origem} para {self._destino} em {self._data}"

class VooEconomico(Voo):
    def calcular_preco(self):
        return 200

class VooExecutivo(Voo):
    def calcular_preco(self):
        return 500

class VooPrimeiraClasse(Voo):
    def calcular_preco(self):
        return 1000

