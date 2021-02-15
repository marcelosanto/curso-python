"""
Operadores Lógicos
and, or, not,
in e not in
"""
# a = 1
# nome = 'Marcelo Santos'

# if not a:
#     print("Valor falso")

# if 'o' in nome:
#     print("Existe a letra 'O' no seu nome.")

# if 'b' not in nome:
#     print("Não existe a letra 'B' no seu nome.")

# Sistema de login fake bem simples

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'marcelo'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print("Você está logado no sistema")
else:
    print("Usuário ou senha inválidos")
