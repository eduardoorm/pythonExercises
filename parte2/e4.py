# Escribir un programa que le diga al usuario que ingrese una cadena.
# El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

cadena = input("Ingresa una cadena")
mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=0
for i in cadena:
    for j in mayusculas:
        if(i==j):
            s=s+1
            print(s)

print(f'tiene {s} mayusculas')