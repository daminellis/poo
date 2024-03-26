class Quarto:
    def __init__(self, numero, preco_diaria):
        self._numero = numero
        self._preco_diaria = preco_diaria
        self._disponivel = True

    def calcular_preco_estadia(self, num_diarias):
        return self._preco_diaria * num_diarias

    def verificar_disponibilidade(self):
        return self._disponivel

    def reservar(self):
        if self._disponivel:
            self._disponivel = False
            print(f"Quarto {self._numero} reservado com sucesso!")
        else:
            print(f"Quarto {self._numero} não está disponível para reserva.")


class QuartoSimples(Quarto):
    def __init__(self, numero):
        super().__init__(numero, preco_diaria=100)


class QuartoDuplo(Quarto):
    def __init__(self, numero):
        super().__init__(numero, preco_diaria=150)


class Suite(Quarto):
    def __init__(self, numero):
        super().__init__(numero, preco_diaria=250)
