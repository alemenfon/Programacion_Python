'''
Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
'''

lista=["Di","Buen","dia","a","papa"]


def cadenaInvertida(lista):
    listaReverse=[]
    for i in range(len(lista)-1,-1,-1):
        listaReverse.append(lista[i])    
    return listaReverse    
print(cadenaInvertida(lista))
        