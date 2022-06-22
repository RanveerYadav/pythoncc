class Employee:
    name = 'Ranveer'
    localtion = 'Vikhroli'
    salary = 500

    #this will print 500, 1000, 500
    # def changeSalary(self, sal):
    #     self.salary = sal

    #this will print 500, 1000, 1000
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal


emp = Employee()
print(emp.salary)
emp.changeSalary(1000)
print(emp.salary)
print(Employee.salary)