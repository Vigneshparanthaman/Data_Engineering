import datetime
today = datetime. date.today()
year = today.year
print(year)


"""
class Company:
    def __init__ (self,cname):
        self.cname=cname
    def displayCname(self):
        print("Company Name: ", self._cname)
    def address(self):
        return "Technopark phase 2 Trivendrum";


class Employee:
    def __init__(self,fname,lname,designation,yob):
        self._fname = fname;
        self._lname = lname;
        self._designation = designation;
        self._yob = yob;
    def getEmpDetails (self):
        print("fullname: ", self._fname," ", self._lname)
        print("yob: ", self._yob)
        print("Designation: ", self._designation)

e1= Employee ("Parag", "Joshi", "Developer", 1234)
e2= Employee ("Vignesh", "Paranthaman", "SDE", 1994)
e3= Employee ("Gobi", "Thaman","HR",1993)

e1.getEmpDetails()
e2.getEmpDetails()
e3.getEmpDetails()
"""
"""--------------------------------------------------------"""
"""
class Company:
    
    def __init__ (self,cname):
        self._cname=cname
    def displayCname(self):
        print("Company Name: ", self._cname)
    def address(self):
        return "Technopark phase 2 Trivendrum";


class Employee:
    isMarried = True
    empcount = 0
    def __init__(self,fname,lname,designation,yob):
        self._fname = fname;
        self._lname = lname;
        self._designation = designation;
        self._yob = yob;
        self._age = year-yob

        Employee.empcount +=1
        
    def getEmpDetails (self):
        print("fullname: ", self._fname," ", self._lname)
        print("yob: ", self._yob)
        print("Designation: ", self._designation)
        print("Marital Status: ", self.isMarried)

e1= Employee ("Parag", "Joshi", "Developer", 1234)
e1.isMarried = False
e2= Employee ("Vignesh", "Paranthaman", "SDE", 1994)
e3= Employee ("Gobi", "Thaman","HR",1993)

e1.getEmpDetails()
e2.getEmpDetails()
e3.getEmpDetails()"""
"""----------------------------------In-heritance--------------------------------------------------"""
class Company:#In-heritance
    
    def __init__ (self,cname):
        self._cname=cname
    def displayCname(self):
        print("Company Name: ", self._cname)
    def address(self):
        return "Technopark phase 2 Trivendrum";
    
class Employee(Company):
    isMarried = True
    empcount = 0
    def __init__(self,cname,fname,lname,designation,yob):
        self._cname = cname;
        self._fname = fname;
        self._lname = lname;
        self._designation = designation;
        self._yob = yob;
        self._age = year-yob #Encabsulation - age is hiding from the year

        Employee.empcount +=1
        
    def getEmpDetails (self):
        self.displayCname()#Poly-morfisum
        print("fullname: ", self._fname," ", self._lname)
        print("yob: ", self._yob)
        print("Designation: ", self._designation)
        print("Marital Status: ", self.isMarried)

    def address(self):
        print ("Company Address: ", super().address())
        print("Employee Address: Ginger Hotel Technopart Phasel") 

e1= Employee ("UST","Parag", "Joshi", "Developer", 1234)
e1.isMarried = False
e2= Employee ("TCS","Vignesh", "Paranthaman", "SDE", 1994)
e3= Employee ("CTS","Gobi", "Thaman","HR",1993)

e1.getEmpDetails()
e2.getEmpDetails()
e3.getEmpDetails()
e1.address()
e2.address()
e3.address()





























