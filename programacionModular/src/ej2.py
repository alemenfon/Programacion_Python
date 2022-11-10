'''
Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
'''

lista=[1,2,3,4,5,6,7,8,9,10]

def desplazarPosicion(lista):
    posicionAnterior=lista[0]
    posicionNueva=0
    
    lista[0]=lista[(len(lista))-1]
   
    for i in range(1,len(lista)):
        posicionNueva=lista[i]
        lista[i]=posicionAnterior
        posicionAnterior=posicionNueva
    return lista

print(lista)
print(desplazarPosicion(lista))