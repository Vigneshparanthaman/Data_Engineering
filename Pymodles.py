""" Modules in python are the python files containing definintions and statements of the same
It contains the python function, classes or variables
modules are saved with an extension.py
module provides the flexibility and organize the code logically
It also provides reuseability
"""

import math
import random as rd
import sys
import os
import Utility
import Salarycalculator

print ( math.factorial(5))
aoc = 2*math.pi*math.pow(5,2)
print(aoc)


print(rd.random())
print("Random number between 1 to 10: ", math.floor(rd.random()*11))
print("Random number between 10 to 99 in steps of 10: ", rd.randrange(10,99,10))
print("Random number between 10 to 99: ", rd.randint(10,99))

print(sys.modules)
print(sys.path)
print(os.name)
print(os.getcwd)

#print(dir(Utility))
print(Utility.isLeapYear(1900))
print("Preffered payment mode is ", Utility.payment_modes[1])
print("Default Gender selected ", Utility.gender[2])

Salarycalculator.calculateSalary()









c=math.remainder(20,3)
print("printing the remainder: ",c)

