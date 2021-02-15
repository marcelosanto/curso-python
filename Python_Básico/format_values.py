"""
Formatando valores com modificadores

:s - Text (strings)
:d - Inteiros (int)
:f - Numeros de ponto flutuante (float)
:.(Número)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE - s, d ou f)
> - Esquerda
< - Direita 
^ - Centro

"""
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_3 = 128
print(f'{num_3:0^10}')

nome = 'Marcelo Santos'
print(f'{nome:#^50}')

print(nome.lower())  # tudo minusculas
print(nome.upper())  # tudo maiusculas
print(nome.title())  # primeiras maiusculas


nome_formatado = '{n:@^20}'.format(n=nome)
print(nome_formatado)
