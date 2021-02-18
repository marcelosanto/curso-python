lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 8],
    ['P4', 9],
    ['P5', 25],
    ['P6', 39],
]
# ordenando lista com funcoes anonimas *lambda
# lista.sort(key=lambda x: x[1])
# print(lista)

# sem alterar a lista original
print(sorted(lista, key=lambda x: x[1]))
print(lista)
