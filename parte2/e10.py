# Escriba una función es_bisiesto() que determine si un año determinado es un año
# bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def es_bisiesto(anio):
    if(anio%4==0 and anio%100!=0):
        return True
    return False

anio = int(input("Por favor ingrese un año"))
isbisiesto = es_bisiesto(anio)
print(f"el año {anio} ¿es bisiesto?:",isbisiesto )