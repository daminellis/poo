class Acervo:
    def __init__(self, titulo, disponivel=True):
        self.titulo = titulo
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"{self.titulo} foi emprestado com sucesso!")
        else:
            print(f"{self.titulo} não está disponível no momento.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"{self.titulo} foi devolvido.")
        else:
            print(f"{self.titulo} já está disponível.")

    def consultar_disponibilidade(self):
        if self.disponivel:
            print(f"{self.titulo} está disponível para empréstimo.")
        else:
            print(f"{self.titulo} não está disponível no momento.")


class Livro(Acervo):
    def __init__(self, titulo, autor, disponivel=True):
        super().__init__(titulo, disponivel)
        self.autor = autor


class Revista(Acervo):
    def __init__(self, titulo, editora, disponivel=True):
        super().__init__(titulo, disponivel)
        self.editora = editora


class CD(Acervo):
    def __init__(self, titulo, artista, disponivel=True):
        super().__init__(titulo, disponivel)
        self.artista = artista


