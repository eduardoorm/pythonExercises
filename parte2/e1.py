#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), 
#solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
# Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(list):
    mayor=0
    for i in list:
        if(i>mayor):
            mayor=i
    
    return mayor

nmayor= max_in_list([1,9,3,20,0])
print(f'el numero mayor es {nmayor}')