'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de
 2e, 
 1e, 
 50 céntimos, 
 20 céntimos o 
 10 céntimos)

'''

euro_2=int(input("Monedas de 2: "))
euro_1=int(input("Monedas de 1: "))
cent_50=int(input("Monedas de 50: "))
cent_20=int(input("Monedas de 20: "))
cent_10=int(input("Monedas de 10: "))

totalEuros=euro_2*2+euro_1*1
totalCentimos=cent_50*50+cent_20 *20+cent_10*10

totalEuros=totalEuros + (totalCentimos//100)
totalCentimos=totalCentimos%100



print(f"El total es: {totalEuros} euros y {totalCentimos} centimos")







