'''
Design a function called lowCaseInString that has a string of characters as parameter, the
method should return how many of those characters are lowcase letters.

'''
cadena="ALEjandra"
def lowCaseInString(cadena):
    lower="abcdefghijklmnñopqrstuvwxyz"
    areLower=0
    for letra in cadena:
        if letra in lower:
            areLower+=1
    return areLower

print(lowCaseInString(cadena))
