'''
Diseña un programa que reciba el tamaño de una secuencia numérica y muestre en
una única línea cada una de las siguientes secuencias. Si se recibe el número 6 se
imprimiría:
a. 1, -5, 25, -125, 625, -3125
b. 1, -1, 0, 1, -1, 0
c. 1, 3, 9, 27, 81, 243
'''

cantidad=int(input("Escriba una secuencia: "))
tipoA=1
tipoB=1
tipoC=1

cadenaA=""
for i in range(1, cantidad+1):
    tipoA*=-5
    if i<cantidad:
        cadenaA+=str(tipoA) + ", "
    else:
        cadenaA+=str(tipoA)       
print(cadenaA)

cadenaC=""
for i in range(1, cantidad+1):
    tipoC*=3 
    if i<cantidad:
        cadenaC+=str(tipoC)+ ", "
    else:
        cadenaC+=str(tipoC)
         
print(cadenaC)




     

  
  
    