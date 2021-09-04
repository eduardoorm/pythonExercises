# Ejercicio 5
# Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista con los elementos únicos de la lista original. 
# No tienen porque estar en el mismo orden.
import numpy as np
def elimina_duplicados(list):
    return set(list)


lista= [1,23,2,4,2]
newlista = elimina_duplicados(lista)

print(np.array(newlista))