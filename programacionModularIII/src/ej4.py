'''
Design a function called numberInString that has a string of characters as parameter, the
method should return how many of those characters are numbers.
'''
cadena="Alejandra12345"
def numberInString(cadena):
    number="0123456789"
    areNumber=0
    for c in cadena:
        if c in number:
            areNumber+=1       
    return areNumber

print(numberInString(cadena))