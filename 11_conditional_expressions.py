#below will get printed
a = 13
if (a == 13):
    print('I am in')

#below will not get printed
b = '13'
if (a == b):
    print('I am in 2')

#elif will get printed
b = '13'
if (a == b):
    print('I am in 2')
elif (a != b):
    print('Elif print')

#check age
age = int(input('Enter your age for entry in club: '))
if age >= 18:
    print('Welcome to the club')
else:
    print('You are not allowed to enter club. Minimum age required is 18')

#check year
year = int(input('Enter current year'))
if year == 2022:
    print('You are correct')
else:
    print('You are wrong')

#conditional operators
#and operator
num = 100
if num < 101 and num > 50:
    print('The number is', num)
else:
    print('Number doesn"t meet criteria')

#or operator
name = 'Ranveer'
if name == 'Ranveer' or name == 'Yadav':
    print('The name is', name)
else:
    print('Name doesn"t matched criteria')

#in operator
city = str(['Mumbai','Pune','Nashik','Nagpur'])
print('Mumbai' in city)
