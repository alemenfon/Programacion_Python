'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
puede calcular?
'''
import math;

num=int(input("Introduzca un numero: "))

r_cuadrada=math.sqrt(num)
print(f"La raíz cuadrada de {num} es: {r_cuadrada}")

r_cubica=num**(1/3)
print(f"La raíz cuadrada de {num} es: {r_cubica}")


