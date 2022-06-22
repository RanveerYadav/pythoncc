#strings
name = 'Ranveer'
city = "Mumbai"
state = '''Maharashta'''
print(name)
print(city)
print(state)
print(type(name))
print(type(city))
print(type(state))

#string slicing
name = 'Raja'
print(name[0])
print(name[1])
print(name[2])
print(name[-3])
print(name[-2])
print(name[-1])
print(name[0:2])
print(name[1:3])
print(name[:3]) #same as [0:3]
print(name[1:]) #same as [1:till last]

#string skipping
env = 'WorldIsBeautiful'
#3rd param is for skip
print(env[0::2]) #skips 1 character
print(env[0::3]) #skips 2 characters

#string other functionalities
animal = 'elephant is huge'
print(len(animal))
print(animal.endswith('huge'))
print(animal.count('e'))
print(animal.capitalize())
print(animal.find('is'))
print(animal.replace('is','are'))