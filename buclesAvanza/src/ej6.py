'''
Juan recibe dos tipos de regalos de cumpleaños según el año en el que esté: si el
año es impar su familia le regala un puzzle; si es par recibe dinero.
Cada nuevo cumpleaños recibe más regalos: así, cada año que recibe puzzles
obtiene el doble que el anterior; sin embargo, si se trata de dinero recibe 15€ más
que en la anterior ocasión.
Elabora un programa que calcule cuántos regalos ha recibido en total Juan, para una
edad determinada sabiendo que en el primer cumpleaños le regalaron un puzzle y
en el segundo 20€.
Ejemplo: 1 año ⇒ 1 puzzle
Ejemplo: 2 años ⇒ 1 puzzle y 20€ (tenía un puzzle y recibe 20€)
…..
…..
Ejemplo: 7 años ⇒ 15 puzzles y 105€ (tenía 105€ y recibe 8 puzzles)


2 VARIABLE RECIBE Y ACUMULA TANTO PARA PUZZLE COMO PARA DINERO
'''

edad=int(input("Introduzca la edad de Juan: "))

recibePuzzle=1
acumulaPuzzle=1

recibeDinero=20
acumulaDinero=0
        
for i in range(2,edad+1):
    if i%2==0: 
        acumulaDinero+=recibeDinero
        recibeDinero+=15
    else:
        recibePuzzle*=2
        acumulaPuzzle+=recibePuzzle

print(f"A la edad de {edad} años, tendrá {acumulaPuzzle} puzzles y {acumulaDinero}€")
    

