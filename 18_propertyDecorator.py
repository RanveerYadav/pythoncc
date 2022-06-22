class Employee:
    salary = 1000
    bonus = 500

    @property
    def totalSalary(self):
        return self.salary + self.bonus

emp = Employee()
print(emp.totalSalary)