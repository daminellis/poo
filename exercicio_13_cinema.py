class Ingresso:
    def __init__(self, preco_base):
        self.preco_base = preco_base
        self.disponibilidade = True

    def calcular_preco(self):
        return self.preco_base

    def verificar_disponibilidade(self):
        return self.disponibilidade

    def reservar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            return True
        else:
            return False


class IngressoVIP(Ingresso):
    def __init__(self, preco_base, taxa_vip):
        super().__init__(preco_base)
        self.taxa_vip = taxa_vip

    def calcular_preco(self):
        return self.preco_base + self.taxa_vip


class Ingresso3D(Ingresso):
    def __init__(self, preco_base, taxa_3d):
        super().__init__(preco_base)
        self.taxa_3d = taxa_3d

    def calcular_preco(self):
        return self.preco_base + self.taxa_3d


