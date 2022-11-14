'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
'''

hora1=int(input("Introduzca una hora: "))
minuto1=int(input("minutos: "))
segundo1=int(input("segundos: "))

hora2=int(input("Introduzca una segunda hora: "))
minuto2=int(input("minutos: "))
segundo2=int(input("segundos: "))

if hora1>=0 and hora1<=23 and hora2>=0 and hora2<=23 and minuto1>=0 and minuto1<=59 and minuto2<=59 and segundo1>=0 and segundo2<=59 and segundo2>=0 and segundo2<=59:
    
    if hora1<hora2:
        print("La hora 1º es menor")

    elif hora2<hora1:
        print("La hora 2 es menor")

    else: 
        
        if minuto1<minuto2:
            print("La hora 1º es menor")
  
        elif minuto2<segundo1:
            print("La hora 2º es menor")
    
        else:
            if segundo1<segundo2:
                print("La hora 1º es menor que la hora 2")
            elif segundo2<segundo1:
                print("La hora 2º es menor")
            else:
                print("Las horas coinciden")
    
else:
    print("Introduzca una hora correcta")
        