# Para un número N imprimir su tabla de multiplicar.
from random import randint

n = randint(1,13)

for i in range(1,13):
    print(f'{i} * {n} = {i*n}')