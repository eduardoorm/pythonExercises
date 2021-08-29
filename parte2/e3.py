# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, 
# y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(list,n):
    newArray=[]
    for i in list:
        if(len(i)>n):
            newArray.append(i)
        
    return newArray
    

palabras=filtrar_palabras(["hola","terremoto","pan"],3)
print(palabras)

