'''
Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente.
'''

mes=int(input("Numero del 1 al 12: "))

if mes >=1 and mes <=12:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        print("El mes tiene 31 dias")
    elif mes==4 or mes==6 or mes==9 or mes==11:
        print("El mes tiene 30 dias")
    else:
        print("El mes tiene 28 días")
else:
    print("Introduzca mes correcto")



