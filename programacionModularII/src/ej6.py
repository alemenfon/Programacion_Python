'''
"6. Design a method called getNumberOfDigits that receives one number (it can be
real, integer, positive or negative) and should return the number of digits it contains. If
the parameter is not valid the method should return None. Extend this function to
other numeric systems (hexadecimal, decimal, binary, octal).
'''

def getNumberOfDigits(number):
    digitos=0
    cont=0
    cadNumber=str(number).upper()
    
    for c in cadNumber:
        if c in "GHIJKLMNÑOPQRSTUVWXYZ":
            digitos=None
        elif c==".":
            cont+=1
    return digitos
print(getNumberOfDigits("16.5"))
    