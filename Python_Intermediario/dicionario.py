# Dicionario
# d1 = {'chave1': 'valor da chave'}
# d1['nova_chave'] = 'Valor da nova chave'

# Outra forma de criar um dicionario
# d1 = dict(chave1='valor da chave', chave2='valor da outra chave')

# d1 = {
#     'chave1': 'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'Tupla'
# }

# del d1['chave1']  # apagando chave do dicionario

# for x, i in enumerate(d1):
#     print(x, d1[i])

# for k, v in d1.items():
#     print(k, v)

clientes = {
    'cliente1': {
        'nome': 'Marcelo',
        'sobrenome': 'Santos'
    },
    'cliente2': {
        'nome': 'Alice',
        'sobrenome': 'Santos'
    },
    'cliente3': {
        'nome': 'Gabriel',
        'sobrenome': 'Rocha'
    },
    'cliente4': {
        'nome': 'Ezequias',
        'sobrenome': 'Santos'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo: {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
