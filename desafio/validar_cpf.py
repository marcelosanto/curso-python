cpf = input('Qual e o seu cpf? ')

calc = []
resul = []

for i, cp in enumerate(cpf, 2):
    calc.append(int(cp))
    resul.append(i)

# print(calc)
test = resul[::-1]
rsultado = []

for y, x in enumerate(calc):
    rsultado.append(x * test[y])

soma = 0
for h in rsultado:
    soma += h

if soma:
    rosult = 11-(soma % 11)
    if rosult > 9:
        calc.append(0)
    else:
        calc.append(rosult)


for i, cp in enumerate(calc, 2):
    resul.append(i)

# print(calc)

test = resul[::-1]
rsultado = []

for y, x in enumerate(calc):
    rsultado.append(x * test[y])

soma = 0
for h in rsultado:
    soma += h

if soma:
    rosult = 11-(soma % 11)
    if rosult > 9:
        calc.append(0)
    else:
        calc.append(rosult)
print(calc)
