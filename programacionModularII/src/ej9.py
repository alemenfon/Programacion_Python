'''
Design a method called getPrimeDivisors that receives a positive number as a
parameter and returns a list containing its prime divisors. If the parameter is not valid
the method should return None.
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
print(isPrime(10))

def getPrimeDivisors(number):
    divisores=[]
    cont=0
    for i in range (1,number):
        if number%i == 0:
            divisores.append(i)
    if number > 0:
        return divisores
        
print(getPrimeDivisors(10))