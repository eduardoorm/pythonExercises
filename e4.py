# 4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def IsVocal(char):
    vowels=["a","e","i","o","u"]
    for i in vowels:
        if(char == i):
            return True
    return False

vowelResponse = IsVocal("s")
print(f'¿Es vocal? : {vowelResponse}')
