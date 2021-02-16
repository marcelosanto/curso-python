"""
Split, join, Enumerate in Python
*  split -> dividir uma string # (str)
*  join -> Juntar uma lista # (str)
*  enumerate -> Enumarar elementos da lista # (objetos iteráveis)
"""

# string = 'O Brasil é o país do futebol, o Brasil é penta.'
# lista = string.lower().split(' ')

# # for valor in lista:
# #     print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase.')

# palavra = ''
# contagem = 0

# for valor in lista:
#     qtd_vezes = lista.count(valor)

#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor

# print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')

# string = 'O Brasil é penta.'
# lista = string.split(' ')
# # string_2 = ' '.join(lista)

# # print(string_2)

# for i, valor in enumerate(lista):
#     print(i, valor)

lista = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
]

# for i, valor in lista:
#     print(i, valor)

n1, n2, n3, n4, n5 = lista

print(n3)
