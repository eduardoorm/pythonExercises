#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(list):
    mayor=""
    for i in list:
        if len(i)>len(mayor):
            mayor=i
    
    return mayor


maxValue=mas_larga(["hola","terremoto","pan"])

print(f'cadena mas larga : {maxValue}')