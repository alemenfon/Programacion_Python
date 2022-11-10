'''
Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000).
'''

from random import randint

lista=[]
for i in range(10):
    lista.append(randint(0, 10))

def obtenerMayor(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    
    return mayor

print(lista)
print(obtenerMayor(lista))

print("--------------------------------------------")

def obtenerMenor(lista):
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]< menor:
            menor=lista[i]
    return menor

print(lista)
print(obtenerMenor(lista))

print("--------------------------------------------")


lista2=[1]
def sumaNumeros(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma
    

print(lista)
print(sumaNumeros(lista))

print("--------------------------------------------")

def obtenerMedia(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]     
      
    return suma/float(len(lista))

print(lista)
print(obtenerMedia(lista))

print("--------------------------------------------")


def sustituirNumero(lista,numSustituto):
    for i in range(len(lista)):
        if numSustituto==lista[i]:
            lista[i]=numSustituto
    return lista

print(lista)
print(sustituirNumero(lista,7))







   


