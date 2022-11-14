'''
La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

'''

minuto=int(input("Minutos: "))
dia=str(input("Dia: Domingo D u otro día O:  "))
turno=str(input("Turno: M o T: "))

if minuto<=5:
    costeLlamada=5
elif minuto<=8:
    costeLlamada=(minuto-5)*0.8+5
elif minuto<=10:
    costeLlamada=(minuto-8)*0.7+5
else:
    costeLlamada=(minuto-10)*0.5+5

if dia=="D":
    impuesto=costeLlamada*0.03
elif dia=="O" and turno=="M":
    impuesto=costeLlamada*0.15
elif dia=="O" and turno=="T":
    impuesto=costeLlamada*0.10
    
print(f"El coste de la llamada es:{costeLlamada} Y el impuesto que se le aplica es:{impuesto} y El el total de la llamada{impuesto+costeLlamada}" )

    
    

