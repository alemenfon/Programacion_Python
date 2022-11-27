'''
Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.
'''
palabra="Abaco".lower()
def contarVocalesDistintas(palabra):
    vocales="aeiou"
    vocalesPalabra=[]
    for c in palabra:
        if c in vocales:
            if c not in vocalesPalabra:
                vocalesPalabra.append(c)
    return len(vocalesPalabra)

print(contarVocalesDistintas(palabra))
        