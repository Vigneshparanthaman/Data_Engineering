def isLeapYear(year):
    if (year%400 == 0 or (year % 100 != 0 and year %4 == 0)):
        return str(year)+" is Leap year"
    else:
        return str(year)+" is not Leap year"

payment_modes = ["Debit","Netbanking","Credit"]
gender = {1:"Male", 2:"Female", 3:"Trangender"}
