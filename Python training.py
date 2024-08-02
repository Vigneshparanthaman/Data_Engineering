Year = int(input("Enter the year: "))
#print(type(Year))
"""
if (Year%400 == 0):
    print (Year, " is Leap year")
else:
    if (Year%100!=0):
        if(Year%4 == 0):
            print (Year, " is Leap year")
        else:
            print(Year, " is not Leap year")
    else:
        print(Year, " is not Leap year")
        
"""
"""
if (Year%400 == 0):
    print (Year , " is leap year")
elif (Year%100!=0 and Year %4 == 0):
    print (Year, " is Leap year")
else:
    print(Year, " is not Leap year")

"""


if (Year%400 == 0 or (Year%100!=0 and Year%4 == 0)):
    print(Year, " is Leap year")
else:
    print(Year, " is not Leap year")


































