# Exercicio 1
# def oi_cara():
#     return 'Eae Man!!'


# def mestre(funcao):
#     return funcao()


# print(mestre(oi_cara))

# Exercicio 2

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oie {nome}'


def saudar(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Marcelo')
print(executando)

executando2 = mestre(saudar, 'Marcelo', 'Bom dia:')
print(executando2)
