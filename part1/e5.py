# 5- Escribir una función sum() y una función multip() que sumen y multipliquen 
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def sum(list):
    s=0
    for i in list:
        s=s+i

    return s

def multip(list):
    m=1
    for i in list:
        m=m*i
    
    return m

print(f' Suma: {sum([1,2,3,4])}')
print(f' Multiplicación: {multip([1,2,3,4])}')