from exercicio_1_func import Gerente, Programador, Analista

# solicitar os detalhes dos funcionários
while True:
    tipo_funcionario = input("Digite o tipo de funcionário que deseja adicionar (gerente/programador/analista): ").lower()

    if tipo_funcionario not in ["gerente", "programador", "analista"]:
        print("Tipo de funcionário inválido. Por favor, tente novamente.")
        continue

    if tipo_funcionario == "gerente":
        nome_gerente = input("Digite o nome do gerente: ")
        salario_base_gerente = float(input("Digite o salário base do gerente: "))
        bonus_gerente = float(input("Digite o bônus do gerente: "))
        novo_funcionario = Gerente(nome_gerente, salario_base_gerente, bonus_gerente)
    elif tipo_funcionario == "programador":
        nome_programador = input("Digite o nome do programador: ")
        salario_base_programador = float(input("Digite o salário base do programador: "))
        linguagem_programador = input("Digite a linguagem do programador: ")
        horas_extra_programador = int(input("Digite as horas extras do programador: "))
        novo_funcionario = Programador(nome_programador, salario_base_programador, linguagem_programador, horas_extra_programador)
    else:  # tipo_funcionario == "analista"
        nome_analista = input("Digite o nome do analista: ")
        salario_base_analista = float(input("Digite o salário base do analista: "))
        nivel_analista = input("Digite o nível do analista (junior/pleno/senior): ")
        novo_funcionario = Analista(nome_analista, salario_base_analista, nivel_analista)

    print(f"\nNovo funcionário adicionado:\n{novo_funcionario}\n")

    continuar = input("Deseja adicionar mais funcionários? (sim/não): ").lower()
    if continuar != "sim":
        break
