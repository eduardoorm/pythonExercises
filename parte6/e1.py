#Determinar la cantidad de dígitos de un numero (1- 100000)



from random import randint


number = randint(1,100000)
print(len(str(number)))