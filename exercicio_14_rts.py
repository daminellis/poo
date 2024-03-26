class Unidade:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def mover(self, destino):
        print(f"{self.nome} moveu-se para {destino}.")

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome}.") #porque nao ta funcionando?

    def defender(self):
        print(f"{self.nome} está se defendendo.")


class Soldado(Unidade):
    def __init__(self, nome, vida=100, ataque=10, defesa=5):
        super().__init__(nome, vida, ataque, defesa)

    def atacar(self, alvo):
        print(f"{self.nome} disparou sua arma contra {alvo.nome}.")


class Tanque(Unidade):
    def __init__(self, nome, vida=200, ataque=30, defesa=20):
        super().__init__(nome, vida, ataque, defesa)

    def atacar(self, alvo):
        print(f"{self.nome} disparou seu canhão contra {alvo.nome}.")


class Aeronave(Unidade):
    def __init__(self, nome, vida=150, ataque=50, defesa=10):
        super().__init__(nome, vida, ataque, defesa)

    def atacar(self, alvo):
        print(f"{self.nome} lançou um míssil em direção a {alvo.nome}.")

