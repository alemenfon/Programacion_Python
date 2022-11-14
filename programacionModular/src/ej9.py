'''
Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k.
'''

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num=5

def menoresNum(lista):
    menores=[]
    for i in range(len(lista)):
        if lista[i]<num:
            menores.append(lista[i])
    return menores

print(menoresNum(lista))

def mayoresNum(lista):
    mayores=[]
    for i in range(len(lista)):
        if lista[i]>num:
            mayores.append(lista[i])
    return mayores

print(mayoresNum(lista))

def multiplosNum(lista):
    sonMultiplos=[]
    for i in range(len(lista)):
        if lista[i]%num==0:
            sonMultiplos.append(lista[i])
    return sonMultiplos

print(multiplosNum(lista))

def mostrarResultados(menoresNum,mayoresNum,multiplosNum):
    return menoresNum(lista),mayoresNum(lista),multiplosNum(lista)
print(mostrarResultados(menoresNum, mayoresNum, multiplosNum))
    
            