# Solicitar un número e imprimir los dígitos pares de este.

n = input("Ingrese un numero")

number  = ""
for i in n:
    if(int(i)%2==0):
        number = number + str(i)

print(number)