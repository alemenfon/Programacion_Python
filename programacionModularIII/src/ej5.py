'''
Design a function called palindrome that has a string of characters as parameter, and return
true if it is a palindrome or false in other case. A word is a palindrome, if it is reads the
same from left to right as from right to left, ignoring whites,. For example: "anilina" or "el
abad le dio arroz al zorro" To simplify the problem, you can assume that simple characters
are used, that is, without tildes or diresis.
'''

cadena="anilina"
def palindrome(cadena):
    palindrome=False
    for c in cadena:
        if c==cadena[-1]:
            palindrome= True
        else:
            palindrome=False
    return palindrome

print(palindrome(cadena))
    
