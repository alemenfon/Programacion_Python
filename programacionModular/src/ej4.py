'''
Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.
'''

def mostrarMayor(listaNumeros):
    mayor=0
    
    for i in range(len(listaNumeros)):
        if listaNumeros[i]>mayor:
            mayor=listaNumeros[i]
        else:
            listaNumeros[i]=mayor
    return mayor

def mostrarPares(listaNumeros):
    pares=[]   
    for i in range(len(listaNumeros)):
        if listaNumeros[i]%2==0:
            pares.append(listaNumeros[i])
    return pares

listaNumeros=[]
num=int(input("Numero: "))
while num>0:
    num=int(input("Numero: "))
    listaNumeros.append(num)

        
print(mostrarMayor(listaNumeros))
print(mostrarPares(listaNumeros))
