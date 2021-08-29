# 1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(n1,n2):
    valueMax=""
    if( n1>n2):
        valueMax = n1
    elif(n1<n2):
            valueMax= n2
    else:
        valueMax=n1

    return valueMax

numeroMayor= max(10,5)
print(numeroMayor)