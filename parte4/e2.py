# 2) De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar.
# El programa determinará el total a pagar, como una factura.
# Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando
# diferentes códigos de productos con sus respectivas cantidades, y 
# cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. Te animas?


diccionario = {'camisa':1,'cinturon':2,'zapatos':3,'pantalon':4 , 'calcetines':5,'faldas':6,'gorras':7,'sueter':8,'corbata':9,'chaqueta':10 }
precio = {1:100,2:200,3:293,4:5,5:40,6:40,7:50,8:60,9:23,10:38}

print(f'ELIJA EL PRODUCTO DESEADO:')
print(f'PRODUCTO.......................CODIGO')

rspta= 0

for clave,valor in diccionario.items():
    print(f'{clave}........................{valor}')

while(rspta != 1):
    code = int(input("introduzca un codigo "))
    units = int(input("ingrese el numero de unidades "))
    totalAmount = precio[code]
    totalAmount *= units
    rspta = int(input("SI DESEA SALIR PRESIONE 1 O DE LO CONTRARIO PRESIONE OTRO NUMERO:"))

print("el precio es de ",totalAmount)