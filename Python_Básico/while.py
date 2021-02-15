# While

# while True:  # Loop infinite
#     nome = input('Qual é o seu nome? ')
#     print(f'Olá {nome}')
#     break

# x = 0
# while x < 10:
#     if x == 3:
#         x += 1
#         continue

#     print(x)
#     x += 1

# x = 0


# while x < 10:
#     y = 0
#     while y < 5:
#         print(f'X vale {x} e Y vale {y}')
#         y += 1
#     x += 1

while True:
    print()
    num_1 = input('Qual e o numero: ')
    num_2 = input('Qual e o outro numero: ')
    operador = input('Qual e o operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Voce precisa digitar um numero')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')
