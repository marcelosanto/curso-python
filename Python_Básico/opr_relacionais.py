# == > >= < <= !=
nome = input('Qual e o seu nome? ')
idade = input('Qual e a sua idade? ')

# Limite para pegar empréstimo
idade_limit = int(idade)

if idade_limit >= 20 and idade_limit <= 30:
    print(f'{nome}, Você está apto a pegar empréstimo')
else:
    print(f' {nome} desculpe, mais voce nao possui a idade pra pegar emprestimo')
