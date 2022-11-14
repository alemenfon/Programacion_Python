'''
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de
números primos que queremos mostrar
'''





numeros=int(input("Cuántos números quieres mostar? "))
primos=0
i=0
while i < numeros:
    if i%2 !=0:
        primos+=i
print(primos)
