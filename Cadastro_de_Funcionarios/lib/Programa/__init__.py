import datetime
import random

from Jefferson_Simplicio_Portfólio_Dev.Cadastro_de_Funcionarios.lib.interface import linhas, vazio

quadro_de_funcionarios = []

def opcao(n):
    if n == 1:
        cadastrar()
    elif n == 2:
        listar_funcionarios()
    elif n ==3:
        media_salarial()
    elif n == 4:
        salario_alto()
    elif n == 5:
        salario_baixo()
    elif n == 6:
        finalizar_programa()

def cadastrar():
    funcionario = {}

    funcionario['nome'] = str(input('Nome do funcionario: '))
    funcionario['id'] = random.randint(9999,999999)
    ano_de_nascimento = int(input('Ano de nascimento: '))
    ano_atual = datetime.datetime.today().year
    funcionario['idade'] = ano_atual-ano_de_nascimento
    funcionario['cargo'] = str(input('Cargo: '))
    funcionario['salario'] = float(input('Salário: '))

    quadro_de_funcionarios.append(funcionario)

def listar_funcionarios():
    if len(quadro_de_funcionarios) > 0:
        for i in quadro_de_funcionarios:
            for n, v in i.items():
                print(f'{n} = {v} ')
            print(linhas())
    else:
        vazio()

def media_salarial():
    if len(quadro_de_funcionarios) > 0:
        med = sum(funcionario['salario']
                  for funcionario in quadro_de_funcionarios) / len(quadro_de_funcionarios)
        print(f' A media salarial dos funcionarios listados é : {media_salarial():.2f}')
    else:
        vazio()

def salario_alto():
    if len(quadro_de_funcionarios) > 0:
        maior= max(quadro_de_funcionarios, key = lambda funcionario: funcionario['salario'])
        print(f'Funcionário: {maior["nome"]}\nSalário: R$ {maior["salario"]:.2f}')
    else:
        vazio()

def salario_baixo():
    if len(quadro_de_funcionarios) > 0:
        menor = min(quadro_de_funcionarios, key = lambda funcionario:funcionario["salario"])
        print(f'Funcionário: {menor["nome"]}\n Salário: R$ {menor["salario"]:.2f}')
    else:
        vazio()

def finalizar_programa():
    print('Finalizando programa...')
    exit()
