# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

names = ["juan","eduardo","pedro","julio"]
letter = input("ingrese la letra a buscar")
cant = 0
for i in names:
    if i[0] == letter:
        cant +=1

print("cantidad que comienza con la a:", cant)