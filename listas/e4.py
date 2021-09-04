# Ejercicio 4
# A - Escribe una función llamada "duplicado" que tome una lista y devuelva True si tiene algún elemento duplicado. La función no debe
# modificar la lista.
# B - Crear una función que genere una lista de 23 números aleatorios del 1 al 100 y comprobar con la función anterior 
# si existen elementos duplicados. (Puedes ver el módulo random como guía)

def duplicado(lista):
    l1= lista
    l2 = set(lista)
    if(len(l1)==len(l2)):
        return True
    else:
        return False



lista = [1,3,"hola",7]
var = duplicado(lista)
print(var)