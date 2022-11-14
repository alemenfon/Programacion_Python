'''
Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario
'''

num1=int(input("Numero primero: "))
num2=int(input("Numero segundo: "))

if num1< num2:
    for i in range(num1,num2):
        if i%2==0:
            print(i)
else:
    for i in range(num2,num1):
        if i%2==0:
            print(i)
    