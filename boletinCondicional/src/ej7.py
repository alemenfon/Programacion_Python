'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
'''
estadoCivil=str(input("Intruduzca su estadio civil: S-Soltero, C-Casado, V-Viudo y D-Divorciado: "))
edad=int(input("Introduzca su edad: "))

if edad>50:
    print("Se aplica un 8,5%")
elif edad<35:
    if estadoCivil=="S" or estadoCivil=="D":
        print("Se aplica un descuento del 12%")
    elif estadoCivil=="V" or estadoCivil=="C":
        print("Se aplica un descuento del 11,3%")
         
else:
    print("Se aplica un descuento de un 10,5")