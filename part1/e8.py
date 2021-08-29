#  Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común 
# o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(list1,list2):
    for i in list1:
        for j in list2:
            if j == i:
                return True
    
    return False


print(superposicion("hola mudo","zskx"))