"""
try:
    
    num1=int(input("Enter the number 1: " ))
    num2=int(input("Enter the number 2: " ))
    result = num1/num2
    print(num1,"/",num2,"=","Result")

    x=[7,13,17,19,41]
    x[len(x)]=23
    print(x)

except ZeroDivisionError:
    print("Error: Denominator cannot be zero")
except IndexError:
    print("Error: Index you are using is not present in the list, use insert mothod or check the index position")
except AssertionError:
    print("Error: you have entered odd number")
else:
    print(num)
finally:
    num=0
    print("The program is ended")
"""

yob = int(input("Enter you year of birth: "))
age = 2024-yob
if age < 18:
    raise Exception (f'Entry age for th PG program is greater than 18 and your age is {age}')
else:
    print("You are eligibl for the PG program",age)


def devide(x,y):
    try:
        if y==0:
            raise ZeroDivisionError("Cannot divide by Zero")
        result = x/y
        return result
    except ( ZeroDivisionError, AssertionError):
        print("Error: You have an system error")
