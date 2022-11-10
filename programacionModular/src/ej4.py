'''
Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.
'''

listaNumeros=[]

def mostrarMayor(listaNumeros):
    mayor=listaNumeros[0]
    num=int(input("Numero: "))
    while num>0:
        listaNumeros.append(num)
        num=int(input("Numero: "))
    for i in range(len(listaNumeros)):
        if listaNumeros[i]>mayor:
            mayor=listaNumeros[i]
        else:
            listaNumeros[i]=mayor
    return mayor

print(mostrarMayor(listaNumeros))
        