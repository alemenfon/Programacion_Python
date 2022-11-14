'''
Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato
[3,4] [2,5]
'''

ficha1=[3,4]
ficha2=[2,5]

def fichasEncajan (ficha1,ficha2):
    encaja=False
    
    if ficha1[0]==ficha2[0]:
        encaja=True
    elif ficha1[1]==ficha2[1]:
        encaja=True
    elif ficha1[0]==ficha2[1]:
        encaja=True
    elif ficha1[1]==ficha2[0]:
        encaja=True
    else:
        encaja=False

    return encaja

print(fichasEncajan(ficha1, ficha2))
    