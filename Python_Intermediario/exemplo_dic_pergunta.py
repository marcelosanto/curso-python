perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '5', 'c': '4'},
        'respostas_certa': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 20-7? ',
        'respostas': {'a': '1', 'b': '5', 'c': '13'},
        'respostas_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 12/2? ',
        'respostas': {'a': '1', 'b': '6', 'c': '4'},
        'respostas_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 2*5? ',
        'respostas': {'a': '10', 'b': '5', 'c': '4'},
        'respostas_certa': 'a',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha uma das opções abaixo: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['respostas_certa']:
        print('EHHHH! Você acertou!!!')
        respostas_certas += 1
    else:
        print('AHHHH Não! Você errou!!!')

    print()

qtd_perguntas = len(perguntas)
procentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {procentagem_acerto}% das perguntas.')
