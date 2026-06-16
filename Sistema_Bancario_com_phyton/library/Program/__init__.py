from Jefferson_Simplicio_Portfólio_Dev.Sistema_Bancario_com_phyton.library.interface import linhas

class Conta:
    def __init__(self, nome_usuario, numero_conta):
        self.nome_usuario = nome_usuario
        self.numero_conta = numero_conta
        self.saldo_conta = 0
        self.depositos = []
        self.saques = []

    def opcao (self,n):
        if n == 1:
            self.depositar()
        elif n == 2:
            self.sacar()
        elif n == 3:
            self.ver_extrato()
        elif n == 4:
            self.finalizar_programa()

    def depositar(self):

        try:
            valor = float(input("Digite o valor que você deseja depositar: "))
            if valor <= 0:
                print (linhas())
                print('Impossivel realizar depositos de valores negativos\n'
                      'Tente novamente!')
            else:
                self.saldo_conta += valor
                print (linhas())
                print(f'Exito! Você fez um deposito de {valor}')
                self.depositos.append(valor)
                return self.saldo_conta
        except(ValueError, TypeError, NameError):
            print('Erro! Digite apenas valores numéricos!')
        except KeyboardInterrupt:
            print()
            print('---')
            print('Programa finalizado pelo usuário!')
            exit()

    def sacar(self):

        try:
            # Limite de quantidade de saques
            if len(self.saques) >= 3:
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
            if valor + sum(self.saques) > 500:
                disponivel = 500 - sum(self.saques)

                print(
                    "Limite diário excedido!\n"
                    f"Você ainda pode sacar R$ {disponivel:.2f}"
                )
                return

            # Verificação de saldo
            if self.saldo_conta < valor:
                print(
                    "Saldo insuficiente!\n"
                    f"Saldo disponível: R$ {self.saldo_conta:.2f}"
                )
                return

            # Saque realizado
            self.saldo_conta -= valor
            self.saques.append(valor)

            print(linhas())
            print("Saque realizado com sucesso!")
            print(f"Valor sacado: R$ {valor:.2f}")
            print(f"Saldo atual: R$ {self.saldo_conta:.2f}")

        except ValueError:
            print("Erro! Digite apenas valores numéricos.")

        except KeyboardInterrupt:
            print("\nPrograma finalizado pelo usuário.")
            exit()



    def ver_extrato(self):
        print("="*42)
        print("Extrato")
        print("="*42)

        print(f'Cliente: {self.nome_usuario}')
        print(f'Conta: {self.numero_conta}')

        for i in self.depositos:
            print(f'Depósito: R$ {i:.2f}')
        print('---')
        for i in self.saques:
            print(f'Saque: R$ {i:.2f}')

        if self.saldo_conta > 0:
            print ('---')
            print(f'O valor disponivel em conta para saque é de {self.saldo_conta}')
        else:
            print ('---')
            print('Você não tem saldo em conta!')

    def finalizar_programa(self):
        print (linhas())
        print('Obrigado por utilizar nosso sistema!\n'
              'Finalizando Programa...')
        exit()

