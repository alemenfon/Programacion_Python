'''
Design a function called charactersInString that has a character string and a character as
input parameters and returns how many times that character appears in the string. It should
do if the string and character are lower case or upper case characters.
'''


cadena=input("Introduzca una cadena").lower()
caracter=input("Introduzca un caracter").lower()
def charactersInString(cadena,caracter):
    vecesRepite=0
    
    for letra in cadena:
        if letra==caracter:
            vecesRepite+=1
    return vecesRepite

print(charactersInString(cadena, caracter))