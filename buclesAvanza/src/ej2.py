'''
Diseñar un programa que pida dos números enteros y nos muestre los siguientes
números que son múltiplos del segundo introducido a partir del primero. Por ejemplo,
si introducimos:
13 y 7 ⇒ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77
(a partir de 13 los siguientes 10 múltiplos de 7)
'''
numInicio=int(input("Escribe un numero: "))
multiplo=int(input("Escribe un segundo numero: "))

for i in range (numInicio, numInicio+1):
    if i% multiplo==0:
        print(i)
        
contador=0
mensaje=""

while contador<10:
    if contador<9:
        mensaje+=str(numInicio)+ ","
    else:
        mensaje+=str(numInicio)
        numInicio+=multiplo
        contador+=1
print(mensaje)