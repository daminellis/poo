from exercicio_11_biblioteca import Livro, Revista, CD

livro1 = Livro("Dom Casmurro", "Machado de Assis")
revista1 = Revista("National Geographic", "National Geographic Society")
cd1 = CD("Thriller", "Michael Jackson")

livro1.emprestar()
livro1.consultar_disponibilidade()
livro1.devolver()
livro1.consultar_disponibilidade()
