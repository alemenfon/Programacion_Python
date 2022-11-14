'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE

Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
'''

import math;
ladoA=float(input("Escriba el lado A: "))
ladoB=float(input("Escriba el lado B: "))

hipotenusa=math.sqrt(ladoA**2 + ladoB**2)
print(hipotenusa)