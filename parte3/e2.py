# Escribe un programa que te permita jugar a una versión simplificada del
# juego Master Mind.
#  El juego consistirá en adivinar una cadena de números distintos. 
#Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras).
#  Después el programa debe ir pidiendo que intentes adivinar la
# cadena de números. En cada intento, el programa informará de cuántos números
# han sido acertados (el programa considerará que se ha acertado un número si
# coincide el valor y la posición).
import random
import numpy as np

def compareNumbers(number):
    if(random_number==number):
        return  False
    showTracks(random_number,number)
    return True

def showTracks(random_number,number):
    arrayRandom = list(str(random_number))
    arrayNumber = list(str(number))
    a= np.array(arrayRandom)
    b= np.array(arrayNumber)
    c= np.equal(a,b)
    #el equal no acepta los arrays
    print("valores",type(a))

def generateRandom(cant): 
    # 298
    max= int("9"*cant)
    cantOne= int("1"*(cant-1))
    min= (max/9)-(cant - cantOne)
    aletorio = random.randint(min,max)
    return aletorio

def requestDigit():
    cantdigit = int(input("ingrese una cantidad de digitos del 2 al 9"))
    while(cantdigit<2 or cantdigit>9):  
        cantdigit = int(input("ingrese una cantidad de digitos del 2 al 9"))
    
    return cantdigit

rspta = True
cantdigit= requestDigit()

random_number = generateRandom(cantdigit)

while(rspta):
    number=int(input("Ingrese un numero "))
    rspta = compareNumbers(number)

print("numero correcto")