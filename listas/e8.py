# Para comprobar si una palabra está en una lista se puede utilizar el operador "in", pero sería una búsqueda lenta,
#  ya que busca a través de las palabras en orden.
# Debido a que las palabras están en orden alfabético, podemos acelerar las cosas con una búsqueda de bisección
#  (también conocida como búsqueda binaria), que es similar a lo que haces cuando buscas una palabra en el diccionario.
#  Comenzamos por el centro y comprobamos si la palabra que buscamos está antes o después del centro. Si está antes,
#  se busca solo en la primera mitad, si está después se busca en la otra mitad de la lista. Con esto reduciremos el tiempo de búsqueda

# Escribir una función llamada "bisect" que tome una lista ordenada y una palabra como objetivo, y nos devuelva el
#  índice en el que se encuentra en la lista, en caso de no aparecer en la lista devuelve "No se encontró la palabra".

# Para mejor ayuda, puede revisar el módulo bisect.

