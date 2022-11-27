'''
Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3
'''

cadena=" He estudiado mucho"

def contarPalabras(cadena):
    conPalabra=0
    
    for c in range (len(cadena)-1):
        if cadena[c]==" " and cadena[c+1]!=" ":
            conPalabra+=1        
    return conPalabra
print(contarPalabras(cadena))