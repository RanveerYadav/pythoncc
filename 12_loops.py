#while loop
i = 0
while i < 10:
    print(i)
    i = i + 1

#for loop
#list
fruits = ['apple','mango','banana','watermelon','cherry']
for fruit in fruits:
    print(fruit)
#tuples
cities = ('Mumbai','Pune','Delhi','Nagpur','Varanasi')
for city in cities:
    print(city)
#for with else
for i in range(10):
    print(i)
else:
    print('This is else in for loop...')
#for with break
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print('This is else in for loop...')
#for with continue
for i in range(10):
    if i == 5:
        continue
    print(i)
else:
    print('This is else in for loop...')
#design pattern
n = 5
for i in range(n):
    print('*' * (n-i))

