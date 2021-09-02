# Identificar si la suma de los dígitos de un numero es par o impar.
from random import randint

n1 = randint(10,100)
print("el numero es",n1)
sumDigit, extNum = 0, 0
while n1 != 0:
    extNum = n1 % 10
    n1 //= 10
    sumDigit += extNum

    
print("La suma de los digitos es: {}".format(sumDigit))
