'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
'''

producto=str(input("Elija un tipo de producto: A, B o C"))
precioInicial=float(input("Indique el precio: "))

if (producto=="A" or producto=="B" or producto=="C") and precioInicial >0:
    
    
    if producto=="A":
        descuento=precioInicial*0.07
        precioRebajado=precioInicial-descuento
        print("El precio rejajado es: " + str(precioRebajado))
    
    elif producto=="C" or precioInicial<500:
        descuento=precioInicial*0.12
        precioRebajado=precioInicial-descuento
        print("El precio rejajado es: " + str(precioRebajado))
            
    else:
        descuento=precioInicial*0.09
        precioRebajado=precioInicial-descuento
        print("El precio rejajado es: " + str(precioRebajado)) 
else:
    print("Error, introduzca un producto y un precio válidos")

    
     
    