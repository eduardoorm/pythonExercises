# Construir un pequeño programa que convierta números binarios en enteros.

n = input("ingrese un numero binario")
# 1010010 = 82
entero= 0
c=0

for i in reversed (n):
    mult = (2**c) * int(i)
    entero=entero + mult
    c+=1

print("el numero entero es:", entero)
