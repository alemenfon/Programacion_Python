'''
Design a function called upperCaseInString that has a string of characters as parameter, the
method should return how many of those characters are upper case letters
'''


cadena="ALEjandra"
def upperCaseInString(cadena): 
    upper="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    areUpper=0
    for letra in cadena:
        if letra in upper:
            areUpper+=1
    return areUpper

print(upperCaseInString(cadena))
