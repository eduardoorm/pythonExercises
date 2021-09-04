# Ejercicio 3
# Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista está ordenada en orden ascendente y 
# devuelva False en caso contrario.
# Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.

def ordenada(list):
    for i in range (0,len(list)):
        # print(i,len(list))
        if(i<len(list)-1):
            if(list[i]<=list[i+1]):
                print(list[i+1])
            else:
                return False

    return True


ordenado = ordenada(["a","b"])

print(ordenado)