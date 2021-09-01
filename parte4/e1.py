#    1)
#    Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior
#    a $100.00, el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad
#    en compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al 
#    cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar 
#    el descuento que el cliente recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento,
#    pero si es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  
#    aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, 
#    de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
import random

def showDiscount(bola,descuento,amountPurchases,numberRandom):
    print("Aleatoriamente usted obtuvo una bola ", bola[numberRandom])
    print(f"Felicidades ha resivido un {descuento} de descuento")
    print("su nuevo total a pagar es: ", amountPurchases)

def makeDiscount(n1,amountPurchases):
    desc= amountPurchases*n1
    amountPurchases-=desc
    return amountPurchases

amountPurchases = int(input("Ingrese la cantidad de sus compras"))

if amountPurchases>=100 :
    bola = ["blanco","rojo","azul","verde","amarilla"]
    numberRandom = random.randint(0,4)
    if(bola[numberRandom]=="blanco"):
        print("Aleatoriamente usted obtuvo una bola ", bola[numberRandom])
        print("No tienes descuento")
    elif(bola[numberRandom]=="rojo"):
        amountPurchases=makeDiscount(0.10,amountPurchases)
        showDiscount(bola,10,amountPurchases,numberRandom)
    elif(bola[numberRandom]=="azul"):
        amountPurchases=makeDiscount(0.20,amountPurchases)
        showDiscount(bola,20,amountPurchases,numberRandom)
    elif(bola[numberRandom]=="verde"):
        amountPurchases=makeDiscount(0.25,amountPurchases)
        showDiscount(bola,25,amountPurchases,numberRandom)
    elif(bola[numberRandom]=="amarilla"):
        amountPurchases=makeDiscount(0.50,amountPurchases)
        showDiscount(bola,50,amountPurchases,numberRandom)

else:
    print("usted no entra a la promoción")

