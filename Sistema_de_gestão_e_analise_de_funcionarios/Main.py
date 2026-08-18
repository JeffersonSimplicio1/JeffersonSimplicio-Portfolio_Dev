from Sistema_de_gestão_e_analise_de_funcionarios.lib.interface import *
from Sistema_de_gestão_e_analise_de_funcionarios.lib.Programa import *

while True:
    selecao = menu(['Cadastrar funcionário','Listar funcionários', 'Média salárial', 'Funcionário com maior salário','Funcionário com menor salário', 'Sair'])
    opcao(selecao)
