# 6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(string):
    newstring=''
    for i in reversed(string):
        newstring = newstring + i
    
    return newstring

print(f'{inversa("estoy probando")}')
