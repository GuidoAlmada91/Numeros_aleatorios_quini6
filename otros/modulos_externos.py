from collections import namedtuple

pez = namedtuple("Pez", ["nombre", "especie", "peso"])

pez1 = pez("Pecesin", "Payaso", "5kg")

print(pez1)


#from collections import Counter

#estudiantes = ("Guido Juan Lucas Alejandro")

#print(Counter(estudiantes.split()))

from datetime import datetime
dt = datetime.now()
print(dt.year)
print(dt.month)
print(dt.day)

dt2 = datetime(2000, 11, 15)
print(dt2)

#CALCULAR RAIZ

import math

m = math.sqrt(100)
print(m)