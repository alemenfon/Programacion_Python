'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
'''

num=int(input("Introduzca un numero: "))
if num%2==0 and num %3==0:
    print("El numero es multiplo de 2")
    print("El numero es multiplo de 3")
elif num%2==0:
    print("Es multiplo de 2")
elif num%3==0:
    print("Es multiplo de 3")