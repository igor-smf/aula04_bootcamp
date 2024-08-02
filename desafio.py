def cadastro(nome: str, salario: float, bonus: float):
    return {"nome": nome, "salario": salario, "bonus": bonus}

CONSTANTE_BONUS = 1000

def validar_valor_entrada(mensagem: str):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Por favor, digite um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

lista_funcionarios = []
continuar = True

while continuar:
    nome = input("Digite o seu nome: ").strip()
    if nome.isdigit() or len(nome) == 0 or nome.isspace():
        print("Entrada inválida para o nome.")
        continue

    salario = validar_valor_entrada("Digite o seu salário: ")
    bonus_perc = validar_valor_entrada("Digite o seu bônus: ")

    valor_bonus = CONSTANTE_BONUS + (salario * bonus_perc / 100)

    print(f"\nOlá {nome}, o seu valor bônus foi de {valor_bonus:.2f}")

    lista_funcionarios.append(cadastro(nome, salario, valor_bonus))

    print("\nInformações de nome, salário e bônus armazenados na lista.\n")

    opcao = input("Digite 'sair' para terminar ou qualquer outra tecla para continuar: ")
    continuar = opcao.lower() != 'sair'

print(lista_funcionarios)
