'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
'''

edad=int(input("Introduzca la edad: "))

if edad >=0 and edad <=99:
    if edad>=0 and edad <=12:
        print("Niño")
    elif edad>=13 and edad <=17:
        print("Adolescente")
    elif edad>=18 and edad <=29:
        print("Joven")
    elif edad:
        print("Adulto")
else:
    edad=int(input("Diga una edad correcta: "))