# 1º Exercicio

def saudar(saud, name):
    print(f'{saud} {name}, tenha um ótimo dia.')


saudar('Oiee', 'Marcelo')

# 2° Exercicio


def somar(x, y, z):
    print(f"Resultado: {x} + {y} + {z} = {x + y + z}")


somar(3, 9, 81)

# 3° Exercicio


def percentual(x, y):
    valor = x * y/100
    return x + valor


print(percentual(50, 10))

# 4° Exercicio


def fizzBuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return 'Fizzbuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


print(fizzBuzz(99))
