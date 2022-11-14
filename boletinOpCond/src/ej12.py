'''
Created on 30 sept 2022

@author: ALEJANDRA MENSAQUE
La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida
'''
tipo=str(input("introduzca un tipo A o B: "))
tamano=int(input("introduzca un tamaño 1 o 2: "))
precioInicial=float(input("Introduce el precio inicial: "))

if tipo=="A":
    if tamano==1:
        precioFinal=precioInicial+0.20
        print(f"El precio total a pagar por la uva de tipo A y tamaño 1 es: {precioFinal} euros")
    else:
        precioFinal=precioInicial+0.30
        print(f"El precio total a pagar por la uva de tipo A y tamaño 2 es: {precioFinal} euros")
else:
    if tamano==1:
        precioFinal=precioInicial-0.30
        print(f"El precio total a pagar por la uva de tipo B y tamaño 1 es: {precioFinal} euros")
    else:
        precioInicial=precioInicial-0.50
        print(f"El precio total a pagar por la uva de tipo B y tamaño 2 es: {precioFinal} euros")
        print("")