# Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista 
# donde el primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, el tercer
# elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente.
# Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].

def sumAccumulated(list):
    total=0
    for i in list:
        total= total + i
        yield total
        



numeros= [1,2,8,3]

new =list(sumAccumulated(numeros))

print(new)