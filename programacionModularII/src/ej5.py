'''
Design a method called powerIt that receives two integers and raises the first
number to the second. You may use the product or recursion and check the values. If
no exponent is provided the first number is raised to 0.
'''

def powerIt(num1,num2):
    cont=1
    for i in range(num2):
        cont*=num1  
    return cont
print(powerIt(5, 2))

