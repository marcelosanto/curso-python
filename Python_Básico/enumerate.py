# Enumerate - Enumerar elementos da lista * list

lista = [
    ['Oracle', 'Java', 'SqlServer'],
    ['Python', 'Javascript', 'Typescript'],
    ['Vscode', 'Atom', 'Sublime']
]

for v1, v2 in enumerate(lista):
    print(v1, v2)

"""
[ <-- Enumerate
    (0, ['Oracle', 'Java', 'SqlServer']), 
    (1, ['Python', 'Javascript', 'Typescript']), 
    (2, ['Vscode', 'Atom', 'Sublime'])
]

"""
