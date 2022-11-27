'''
7. Design a method called isPrime that receives one integer positive number greater
than 0 as parameter. The method should return True if the number is prime or False if
not prime. If the parameter is not valid the method should return None.
'''
def isPrime(number):
    esPrimo=True
    if number>0:
        for i in range(2, number):
            if number%i==0:
                esPrimo=False
    else:
        esPrimo=None
        
    return esPrimo

print(isPrime(7))