class salary:
    def __init__ (self, Basicsalary, allowances, deduction):
        self._Basicsalary = Basicsalary
        self._allowances = allowances
        self._deduction = deduction

    def Calculate_total_salary(self):
        gross_salary = self.Basicsalary + sum(self.allowances)
        total_salary = gross_salary - sum(deduction)
        return total_salary

Basicsalary = 50000
allowances = [2000,1500]
deduction = [500,100]

salary_obj = salary(Basicsalary, allowances, deduction)
total_salary= salary_obj.Calculate_total_salary()

print("Total Salary: ",total_salary)
