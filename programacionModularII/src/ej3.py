'''
Design a method called computeDaysInMonth that returns the number of days for
the month and year that are received as arguments. You may use the method
leapYear above. If the values are not valid the method should return -1.

'''
from src.ej2 import isLeapYear

def computeDaysInMonth(mes,year):
    diasmes=[31,28,31,30,31,30,31,31,30,31,30,31]
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    dias=-1
    
    if (mes<1 or mes>12) and (year<1 or year>31):
        dias=-1
    elif mes==2 and isLeapYear(year):
        dias=29
    else:
        for mes in range (len(meses)):
            dias=diasmes[mes]
    return dias

print(computeDaysInMonth(4, 2024))
            
            
    
    
    
