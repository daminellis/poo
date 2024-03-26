from exercicio_3_pers import Guerreiro, Mago, Ladino

while True:
    tipo_personagem = input("Digite qual o tipo de personagem que deseja criar :\n"
                            "Guerreiro\n"
                            "Mago\n"
                            "Ladino\n").lower()
    
    if tipo_personagem not in ["guerreiro","mago","ladino"]:
        print ("Tipo de personagem inválido!! Digite novamente.")
        continue

    if tipo_personagem == "guerreiro":
        nome_guerreiro = input("Digite o nome do seu Guerriero :")
        especie_guerreiro = input("Digite a especie do seu Guerreiro :")
        forca_guerreiro = float(input("digite a força base do seu Guerreiro :"))
        espada_guerreiro = input("Digite qual espada seu Guerreiro usará :")
        escudo_guerreiro = input("Digite qual escudo seu Guerreiro usará :")
        novo_personagem = Guerreiro(nome_guerreiro, especie_guerreiro, forca_guerreiro, espada_guerreiro, escudo_guerreiro)    
    elif tipo_personagem == "mago":
        nome_mago = input("Digite o nome do seu Mago :")
        especie_mago = input("Digite a espécie do seu Mago :")
        forca_mago = float(input("Digite a forca base do seu Mago :"))
        cajado_mago = input("Digite qual será o cajado do seu Mago :")
        livro_mago = input("Digite o nome do livro que seu Mago terá :")
        novo_personagem = Mago(nome_mago, especie_mago, forca_mago, cajado_mago, livro_mago)
    else: #tipo_personagem == "ladino"
        nome_ladino = input("Digite o nome do seu Ladino :")
        especie_ladino = input("Digite a espécie do seu Ladino :")
        forca_ladino = float(input("Digite a forca base do seu Ladino :"))
        adaga_ladino = input("Digite o nome da adaga que seu Ladino usará :")
        funda_ladino = input("Digite qual a funda que seu Ladino usará :")
        novo_personagem = Ladino(nome_ladino, especie_ladino, forca_ladino, adaga_ladino, funda_ladino)

    print(f"\n Novo personagem adicionado!! :\n{novo_personagem}\n")

    continuar = input("Deseja adicionar mais Personagens? (sim/não): ").lower()
    if continuar != "sim":
        break