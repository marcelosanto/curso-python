# Formatar Strings

nome = 'Marcelo'
idade = 29
altura = 1.75
e_maior = idade > 18
peso = 102.9

imc = peso / (altura * altura)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome}, tem, {idade}, de idade e seu imc é, {imc:.2f}')
print('{}, tem, {}, de idade e seu imc é, {:.2f}'.format(nome, idade, imc))
