# Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el 
# código de la categoría de la película y posterior a ello pide que el usuario introduzca el número de días de
# atraso, y así se muestra al  final el total a pagar.

dicCategory = {"Favoritos":2.50,"Nuevos":3.00,"Estrenos":3.50,"Super Estrenos":4.00}
dicCode = {"Favoritos":1,"Nuevos":2,"Estrenos":3,"Super Estrenos":4}
dicRecargo = {1:0.50,2:0.75,3:1.00,4:1.50}

code = int(input("INTRODUZCA EL CODIGO DE LA CATEGORIA DE LA PELICULA"))
daysLate = int(input("INTRODUZCA EL NUMERO DE DIAS DE ATRASO EN LA DEVOLUCION "))

keys= list(dicCode.keys())
recargo = dicRecargo[code] * daysLate
namePelicula  = keys[code-1]
precio = dicCategory[namePelicula]

mount = precio + recargo


print("EL TOTAL A PAAGAR ES : ", mount )



