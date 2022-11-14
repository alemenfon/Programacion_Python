'''
Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario.
'''


lista=[1,2,8,4,5]

def estaOrdenada(lista):
    
    valida=True
    for i in range(1,len(lista)):
        if lista[i]<lista[i-1]:
            valida=False
            
    return valida
        
print(estaOrdenada(lista))