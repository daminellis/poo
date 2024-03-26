from exercicio_6_hotel import QuartoSimples, QuartoDuplo, Suite 

if __name__ == "__main__":
    quarto1 = QuartoSimples(101)
    quarto2 = QuartoDuplo(201)
    quarto3 = Suite(301)

    quarto1.reservar()
    quarto1.reservar()

    print(f"Preço da estadia no quarto simples: ${quarto1.calcular_preco_estadia(3)}")
    print(f"Disponibilidade do quarto duplo: {quarto2.verificar_disponibilidade()}")
    quarto2.reservar()