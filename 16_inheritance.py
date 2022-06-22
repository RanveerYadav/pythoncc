#Code reusablity, extend parent class to child class

#single inheritance
class Circle:
    def circleArea(self, radius):
        return 3.14 * radius * radius

class Rectangle (Circle):
    def rectangleArea(self, len, breath, height):
        return len * breath * height

area = Rectangle()
a = area.circleArea(3)
b = area.rectangleArea(3,4,5)
print(a, b)


#multiple level inheritance
class Soil:
    className = 'Soil class'

    @staticmethod
    def hi():
        print('I am soil class')

class Water:
    className = 'Water class'

class Plant(Soil, Water):
    className = 'Plant class'

s = Soil()
print(s.className)
w = Water()
print(w.className)
p = Plant()
print(p.className)
print(p.hi())


#Multilevel inheritance
class Country():
    def countryName(self):
        print(f'I am a country')

class State(Country):
    def stateName(self, state):
        print(f'I am a state {state}')

class City(State):
    def cityName(self):
        print(f'I am a city')

c = City()
print(c.cityName())
print(c.stateName('Maharashtra'))
print(c.countryName())
