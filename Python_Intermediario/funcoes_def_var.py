variavel = 'valor'


def func():
    print(variavel)

# Não da pra alterar valor de variaveis globais de dentro da função


def func2():
    # global variavel -> Não é uma boa pratica de programação
    variavel = 'Outro valor'
    print(variavel)


func()
func2()
