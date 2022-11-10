'''
Diseñar un programa que muestre, para cada número introducido por teclado, si es
par, si es positivo y su cuadrado. El proceso se repetirá hasta que el número
introducido por teclado sea 0. Por ejemplo:
4 ⇒ es par, positivo y su cuadrado es 16
-7 ⇒ es impar, negativo y su cuadrado es 49
'''

num=1
cuadrado=0

while num !=0:
    
    num=int(input("Introduzca un número: "))
    if num%2==0 and num >0:
        cuadrado=num**2
        print(f"El número {num} es par, positivo y su cuadrado es {cuadrado}")
        
    elif num%2 !=0 and num <0:
        cuadrado=num**2
        print(f"El número {num} es impar, negativo y su cuadrado es {cuadrado}")
          
print("FINALIZADO")