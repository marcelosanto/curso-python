# Operador ternário em Python

# logged_user = True

# msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar.'

# print(msg)

idade = input('Qual é a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas numero.')
else:
    e_de_maior = (int(idade) >= 18)
    msg = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'

print(msg)
