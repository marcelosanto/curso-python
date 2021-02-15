# Entrada de dados

nome = input('Qual o seu nome? ')
idade = input('Qual e a sua idade? ')
ano_nascimento = 2020 - int(idade)

print()
print(f'O {nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}')
