from Jefferson_Simplicio_Portfólio_Dev.Sistema_Bancario_com_phyton.library.interface import *
from Jefferson_Simplicio_Portfólio_Dev.Sistema_Bancario_com_phyton.library.Program import  *


nome_usuario = input('Usuário: ')
numero_conta = int(input('Conta: '))

conta = Conta(nome_usuario, numero_conta)

while True:
    selecao = menu(['Depositar', 'Sacar', 'Extrato', 'Sair' ])
    conta.opcao (selecao)
