# 2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max(n1,n2,n3):
    if (n1>n2 and n1>n3):
        maxValue=n1
    elif(n2>n1 and n2>n3):
        maxValue=n2
    else:
        maxValue=n3
    
    return maxValue

maxi = max(0,4,4)
print(f'el maximo valor es {maxi}')


