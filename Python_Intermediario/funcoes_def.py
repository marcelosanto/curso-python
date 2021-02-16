# Funções - def em Python

def divisao(x=0, y=0):
    if y == 0:
        return

    return x/y


divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('Conta inválida.')
