# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elemtnetos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estao nos dois sets, mas nao em ambos)
s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 6}
s3 = s1 | s2  # -> une os sets
s4 = s1 & s2  # -> une somente os elementos presentes nos dois sets
s5 = s1 - s2  # -> mostra os elementos diferentes do set da esquerda
s6 = s1 ^ s2  # -> mostra os dados diferentes de ambas lista

# print(s3)
# print(s4)
# print(s5)
# print(s6)

l1 = ['Marcelo', 'Alice', 'Gabriel']
l2 = ['Marcelo', 'Alice', 'Gabriel', 'Marcelo',
      'Marcelo', 'Marcelo', 'Marcelo', 'Marcelo', ]

if set(l1) == set(l2):
    print('l1 é igual a l2')
else:
    print('L1 é diferente de L2')
