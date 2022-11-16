'''
Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.
'''

nombres=["Alejandra","Rocío","Jose","Ana","Antonio","Laura","Alba"]
letra="A"

def empiezanPor(nombres,letra):
    nombresEmpiezan=[]
    res="0123456789,.;:-_<>#~$%&/()=?¿¡!^[]{}*-+ªº"
    if (letra in res):
        print("Debe ser un caracter alfabetico")
    else:
        for nombre in nombres:
            if letra in nombre[0]:
                nombresEmpiezan.append(nombre)
    return nombresEmpiezan

print(empiezanPor(nombres, letra))
        
