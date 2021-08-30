# Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y
#  así hasta completar todas las vocales.
# Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(value):
    cantA=cantE=cantI=cantO=cantU=0
    for i in value:
        if i =="a":
            cantA+=1
        elif i == "e":
            cantE+=1
        elif i == "i":
            cantI+=1
        elif i == "o":
            cantO+=1
        elif i == "u":
            cantU+=1
        
    print("a:",cantA,"e:",cantE,"i:",cantI,"o:",cantO,"u:",cantU)
    
value = input("ingrese una cadena")
contar_vocales(value)

            
    
