import random
numeros_aleatorios = []
for i in range(6):
    quini = random.randrange(0, 46)
    numeros_aleatorios.append(quini)
    numeros_aleatorios.sort()
print(numeros_aleatorios)