import random

numeros_aleatorios = []
while len(numeros_aleatorios) < 6:
    quini = random.randrange(1, 46)
    if quini not in numeros_aleatorios:
        numeros_aleatorios.append(quini)

numeros_aleatorios.sort()
print(numeros_aleatorios)