# Ejercicio 6
# Escribe una función que lea las palabras de un archivo de texto (texto.txt) y construya una lista
# donde cada palabra es un elemento de la lista.

doc = open("texto.txt","r")
a =doc.read()
print(a.split())
doc.close()

#lectura
# file_name = 'texto' +'.txt'
# f = open(file_name, 'r')


# c=  f.readline()
# b = f.readline()
# d=  f.readline()

# print(c,b,d)

#escritura
# doc2 = open("texto.txt","w")
# doc2.write("esto es la linea 1\n")
# doc2.write("esto es otra linea \n")
# doc2.write("esta va a ser la ultima linea \n")

# doc2.close()
