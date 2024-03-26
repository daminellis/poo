from exercicio_10_reserva import VooEconomico, VooExecutivo, VooPrimeiraClasse

# Exemplo de uso
if __name__ == "__main__":
    voo_economico = VooEconomico("São Paulo", "Rio de Janeiro", "2024-04-01", 100)
    voo_executivo = VooExecutivo("São Paulo", "Nova York", "2024-05-15", 50)
    voo_primeira_classe = VooPrimeiraClasse("Paris", "Tóquio", "2024-06-20", 20)
    
    print(voo_economico)
    print("Preço do voo econômico:", voo_economico.calcular_preco())
    print("Disponibilidade:", voo_economico.verificar_disponibilidade())
    voo_economico.reservar(2)
    print("Disponibilidade após reserva:", voo_economico.verificar_disponibilidade())
