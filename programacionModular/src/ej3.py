'''
Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.
'''


def solicitarFecha(dia,mes, year):
    mensaje=(f"La fecha en formato largo es {dia} de {mes} de {year}")
    dia=int(input("Dia: "))
    while dia >31:
        dia=int(input("Dia: "))   
    while dia>0:
        mes=int(input("Mes: "))
        while mes not in [1,2,3,4,5,6,7,8,9,10,11,12]:
            mes=input("Mes:")       
        year=int(input("Año: "))
        print(f"La fecha en formato largo es {dia} de {mes} de {year}")
        dia=int(input("Dia: "))
        while dia >31:
            dia=int(input("Dia: "))
    return mensaje

    

print(solicitarFecha(16, 5, 1997))
    
   
   
   
        
        