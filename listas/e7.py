# Ejercicio 7
# Escribe una función llamada "inversa" que busque todas las palabras inversas de una lista.
# Ejemplo de palabras inversas: radar, oro, rajar, rallar, salas, somos, etc...

def inversa(list):
    for i in list:
        cadenaInvertida = i[::-1]  #con esto invertimos una cadena
        if(cadenaInvertida==i):
            print(cadenaInvertida)


inversa(["radar","hola","oro","salas"])