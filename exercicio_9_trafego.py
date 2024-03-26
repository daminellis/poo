import random

class Veiculo:
    def __init__(self, tipo_veiculo):
        self.tipo_veiculo = tipo_veiculo

    def calc_rot(self, origem, destino):
        # Simulação simples: apenas retorna uma rota aleatória
        rota = [origem]
        while rota[-1] != destino:
            next_intersection = random.choice(['A', 'B', 'C', 'D'])  # Simulação de interseções na cidade
            rota.append(next_intersection)
        return rota

    def calc_temp(self, rota):
        # Simulação simples: tempo de viagem baseado no número de interseções
        return len(rota) - 1

class Carro(Veiculo):
    def __init__(self):
        super().__init__("Carro")

class Onibus(Veiculo):
    def __init__(self):
        super().__init__("Ônibus")

class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__("Bicicleta")
