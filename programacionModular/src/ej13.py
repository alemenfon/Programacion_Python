'''
Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.
'''

nombres=["Alejandra","Rocío","Jose","Ana","Antonio"]
letra="A"

def empiezanPor(nombres,letra):
    nombresEmpiezan=[]
    for nombre in nombres:
        if letra in nombre:
            nombresEmpiezan.append(nombre)
    return nombresEmpiezan

print(empiezanPor(nombres, letra))
        