'''
Created on 3 oct 2022

@author: ALEJANDRA MENSAQUE
El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de
autobuses y lo que debe pagar cada alumno por el viaje.

'''

alumno=int(input("Cuantos alumnos: "))

if alumno >=100:
    coste=alumno*65
    print(f"El coste por cada alumno es de {coste}")

elif alumno<=99 and alumno>=50:  
    coste=alumno*70
    print(f"El coste por cada alumno es de {coste}")
elif alumno >=30 and alumno <=49:
    coste=alumno*95
    print(f"El coste por cada alumno es de {coste}")  
else:
    coste=4000
    print(f"El coste por cada alumno es de {coste}")

