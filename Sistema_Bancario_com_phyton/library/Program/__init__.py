from Jefferson_Simplicio_Portfólio_Dev.Sistema_Bancario_com_phyton.library.interface import linhas

saldo_conta = 0
depositos = []
saques = []

def opcao (n):
    if n == 1:
        depositar()
    elif n == 2:
        sacar()
    elif n == 3:
        ver_extrato()
    elif n == 4:
        finalizar_programa()

def depositar():
    global saldo_conta

    try:
        valor = float(input("Digite o valor que você deseja depositar: "))
        if valor < 0:
            print (linhas())
            print('Impossivel realizar depositos de valores negativos\n'
                  'Tente novamente!')
        else:
            saldo_conta += valor
            print (linhas())
            print(f'Exito! Você fez um deposito de {valor}')
            depositos.append(valor)
            return saldo_conta
    except(ValueError, TypeError, NameError):
        print('Erro! Digite apenas valores numéricos!')
    except KeyboardInterrupt:
        print()
        print('---')
        print('Programa finalizado pelo usuário!')
        exit()

def sacar():
    global saldo_conta

    try:
        # Limite de quantidade de saques
        if len(saques) >= 3:
            print("Você já realizou o limite de 3 saques diários.")
            return

        valor = float(input("Digite o valor desejado para saque: "))

        # Valor deve ser positivo
        if valor <= 0:
            print("Valor inválido! Digite um valor maior que zero.")
            return

        # Limite por saque
        if valor > 500:
            print("O valor máximo por saque é R$ 500,00.")
            return

        # Limite diário
        if valor + sum(saques) > 500:
            disponivel = 500 - sum(saques)

            print(
                "Limite diário excedido!\n"
                f"Você ainda pode sacar R$ {disponivel:.2f}"
            )
            return

        # Verificação de saldo
        if saldo_conta < valor:
            print(
                "Saldo insuficiente!\n"
                f"Saldo disponível: R$ {saldo_conta:.2f}"
            )
            return

        # Saque realizado
        saldo_conta -= valor
        saques.append(valor)

        print(linhas())
        print("Saque realizado com sucesso!")
        print(f"Valor sacado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo_conta:.2f}")

    except ValueError:
        print("Erro! Digite apenas valores numéricos.")

    except KeyboardInterrupt:
        print("\nPrograma finalizado pelo usuário.")
        exit()



def ver_extrato():
    global saldo_conta
    print(f'=== Deposito ==='.center(42))
    for i in depositos:
        print(f'{i}')

    print(' === Saques ==='. center(42))
    for i in saques:
        print(f'{i}')

    if saldo_conta > 0:
        print (linhas())
        print(f'O valor disponivel em conta para saque é de {saldo_conta}')
    else:
        print (linhas())
        print('Você não tem saldo em conta!')

def finalizar_programa():
    print (linhas())
    print('Obrigado por utilizar nosso sistema!\n'
          'Finalizando Programa...')
    exit()

