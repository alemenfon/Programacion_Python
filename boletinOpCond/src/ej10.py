'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
 Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.
'''


ladoA=int(input("lado A: "))
ladoB=int(input("lado B: "))
ladoC=int(input("lado C: "))

if(ladoA==ladoB and ladoB==ladoC):
    print("Triangulo equilatero")
elif(ladoA==ladoB and ladoB!=ladoC or ladoB==ladoC) and (ladoC!=ladoA or ladoC==ladoA and ladoA!=ladoB):
    print("Triangulo isosceles")
elif (ladoA!=ladoB and ladoB!=ladoC and ladoC!=ladoA):
    print("Triangulo Escaleno")



 


    
