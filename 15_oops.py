#class
#in class self must always be passed as the first argument, followed by arguments
class Number:
    def sum(self, n1, n2):
        return n1 + n2

num = Number()
sumValue = num.sum(10, 3)
print(sumValue)


#class attribute
class Employee:
    company = 'Google'
    salary = 100

c1 = Employee()
c2 = Employee()
print(c1.company)
print(c2.company)
Employee.company = 'Apple Inc'
print(c1.company)
print(c2.company)


#instance attribue, taking Employee class example
c1.salary = 3000
c2.salary = 4000
print(c1.salary)
print(c2.salary)


#f is written before string to pass variable in the string
class School:
    location = 'Vikhroli'
    def schoolName(self):
        print(f'Name of school is {self.sName} which is located in {self.location}')

    #when passed as static no need for self
    @staticmethod
    def schoolMoto():
        print('Tamosoma Jyotir Gamaya.')

s = School()
s.sName = 'Udhayachal High School'
s.schoolName()
s.schoolMoto()


#__init__ is known as the constructor
class Games:
    #__init__ is contructor
    def __init__(self, gameName, gameOrigin):
        self.gameName = gameName
        self.gameOrigin = gameOrigin
        print('Football is a famous game.')

    def gameDetail(self):
        print(f'{self.gameName} was originated in {self.gameOrigin}')

game = Games('Cricket', 'England')
game.gameDetail()
