'''
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo
'''

limit_inf=int(input("Introduzca el limite inferior"))
limit_sup=int(input("Introduzca el limite superior"))

while limit_inf>=limit_sup:
    print("El limite inferior es mayor que el limite superior, introduzca un valor correcto")
    limit_inf=int(input("Introduzca el limite inferior"))


suma=0
fuera=0
coincide=False
num=int(input("Introduzca número. El número 0 para terminar")) 

while num!=0:

    if num>limit_inf and num<limit_sup:
        suma+=num
    elif num<limit_inf or num>limit_sup:
        fuera+=1
    else:
        coincide=True
    num=int(input("Introduzca número. El número 0 para terminar"))

print(f"La suma de los numeros que están dentro del intervalo es: {suma} ")
print(f"Los numeros fuera del intervalo son: {fuera} ")
if coincide:
    print("Hay numeros que coinciden con el limite del intervalo")
else:
    print("No hay")
    

    

    