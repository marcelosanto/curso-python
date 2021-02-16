# Listas em Python
# lista = ['Oracle', 'Java', 'SqlServer',
#          'Delphi', 'Python', 'Android', 'Oracle']

# # percorrendo a lista
# for list in lista:
#     print(list)

secreto = 'chaves'
digitadas = []
chances = 3

while True:
    if chances < 0:
        print('Você perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUL, a letrar "{letra}" existe na palavra secreta.')
    else:
        print(
            f'AAFFFzzzZ: a letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal voce ganhou!!!! A palavra era {secreto}')
        break
    else:
        print(f'A palavra secreta esta assim {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
