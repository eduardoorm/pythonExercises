# Definir una tupla con 10 edades de personas.
# Imprimir la cantidad de personas con edades superiores a 20.
# Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

edades = []
for edad in range(10):
    newedad =  int(input("ingresa una edad"))
    edades.append(newedad)

cant = 0
for i in edades:
    if i>20:
        cant+=1

print("cantidad de edades mayores a 20:",cant)