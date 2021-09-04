# Ejercicio 2
# Escribe una función llamada "elimina" que tome una lista y elimine el primer y último elemento de la lista y cree una nueva lista 
# con los elementos que no fueron eliminados.
# Luego escribe una función que se llame "media" que tome una lista y devuelva una nueva lista que contenga todos 
# los elementos de la lista anterior menos el primero y el último.

def elimina(list):
    list.pop(0)
    list.pop()
    return list


lista =[1,24,3,4,3,45,6,4]
newList = elimina(lista)
print(newList)