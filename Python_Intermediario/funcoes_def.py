# Funções - def em Python

# def divisao(x=0, y=0):
#     if y == 0:
#         return

#     return x/y


# divide = divisao(8, 0)

# if divide:
#     print(divide)
# else:
#     print('Conta inválida.')

# Funções def em Python - *args **kwargs

def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')


lista = [1, 2, 3, 4, 5, 6]
lista2 = [10, 20, 30, 40, 50, 60]
func(*lista, *lista2, nome='Marcelo', sobrenome='Santos')
