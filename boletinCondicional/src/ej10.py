'''
Created on 28 sept 2022


@author: ALEJANDRA MENSAQUE
Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error.
'''

char=str(input("Introduzca un caracter: "))
num1=int(input("Introduzca un numero: "))
num2=int(input("Introduzca un numero: "))

if char=="+":
    print(num1+num2)
elif char=="-":
    print(num1-num2) 
elif char=="*" :
    print(num1*num2)
elif char=="/":
    print(num1/num2)
elif char=="//":
    print(num1//num2)
elif char=="%":
    print(num1%num2)

else:
    print("ERROR")
    

