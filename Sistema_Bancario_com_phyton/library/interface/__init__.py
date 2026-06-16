def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError, NameError):
            print(f'Por favor, Digite um numero inteiro validor!')
            continue
        except KeyboardInterrupt:
            print(f'\nPrograma finalizado pelo usuario!')
            exit()
        else:
            return n
def linhas(tam = 42):
    return '-'* tam

def cabecalho(txt):
    print(linhas())
    print(txt.center(42))
    print(linhas())

def menu (lista):
    cabecalho("Sistema Bancário")
    c=1
    for i in lista:
        print(f'{c} - {i}')
        c +=1
    print(linhas())
    opc = leia_int('Escolha uma opção: ')
    return opc