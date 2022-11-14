'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra.

'''

precioProducto=float(input("Introduzca el precio del producto: "))

descuento=precioProducto*0.15

preciFinal=precioProducto-descuento
print(preciFinal)