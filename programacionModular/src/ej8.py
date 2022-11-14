'''
Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números.
'''
lista=[]
def pedirNumeros(num):
    num=1
    while num>0:
        num=int(input("Introduzca un número, negativo para terminar: "))
        if num >0:
            lista.append(num)
    return lista

print(pedirNumeros(lista))
                 

def listarPrimos(lista):
    primos=[]
    for i in range(1,len(lista)):
        if lista[i]%i==0:
            primos.append(lista[i])
    return primos
print(listarPrimos(lista))

def sumarNumeros(lista):
    suma=0
    for i in lista:
        suma+=i
        
    return suma

print(sumarNumeros(lista))

def mediaNumeros(lista):
    media=sumarNumeros(lista)/len(lista)
    return media    

print(mediaNumeros(lista))
        
        
        

