'''
Design a method called computeFactorial that receives a positive integer and
returns the factorial for that number. If the number is negative the method should
return None.
'''

def computerFactorial(number):
    factorial=1
    if number >0:
        while number >0:
            factorial=factorial*number
            number-=1
        return factorial
print(computerFactorial(5))   