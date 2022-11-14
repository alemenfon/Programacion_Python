'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
'''
pago=10
total=pago



for i in range(1,21):
    pago*=2
    total+=pago
    print(f"El pago del mes {i} es {pago} euros")

print(f"El total es {total}")
