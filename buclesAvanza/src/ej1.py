'''
Crea un programa que tras preguntar por dos números realice la división del mayor
de ellos por el menor y muestre el resultado de la división, es decir, el cociente y el
resto. Solo puedes utilizar la suma o la resta, pero no otras operaciones.

'''
num1=int(input("Introducir un numero: "))
num2=int(input("Introducir un segundo numero: "))

if num1>num2:
    dividendo=num1
    divisor=num2
else:
    dividendo=num2
    dividor=num1
    
cociente=0
resto=0  


while dividendo>=divisor:
    dividendo-=divisor
    cociente+=1
    resto=dividendo
        
print(f"El resultado de la división  es: cociente: {cociente} y el resto: {resto}")
    
        



    