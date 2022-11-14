'''
Created on 28 sept 2022

@author: ALEJANDRA MENSAQUE
'''

char=str(input("Introduzca un caracter: "))

if char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
    if char=="A":
        print("Es la primera vocal A")
    elif char=="E":
        print("Es la segunada vocal E")
    elif char=="I":
        print("Es la tercera vocal I")
    elif char=="0":
        print("Es la cuarta vocal O")
    elif char=="U":
        print("Es la quinta vocal U")
else:
    print("No es una vocal")