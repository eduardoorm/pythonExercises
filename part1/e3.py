# 3- Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def longitud(text):
    c=0
    for i in text:
        c=c+1
    
    return c

n= longitud("Hola Mundo")
print(f'la cadena tiene una logitud de {n}')