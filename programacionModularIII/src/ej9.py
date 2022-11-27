'''
Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio
'''
cadena="curso de programacion"

def modificarCadena(cadena):
    cons="bcdfghjklmnñpqrstvwxyz"
    vocal="aeiou"
    cadenaCons=""
    cadenaVocal=""
    cadenaModifica=""
    for c in cadena:
        if c in cons:
            cadenaCons+=c
        elif c in vocal:
            cadenaVocal+=c
    cadenaModifica=cadenaCons + cadenaVocal
    return cadenaModifica.replace(" ", "")

print(modificarCadena(cadena))
            
    