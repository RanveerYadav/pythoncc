#list is container of data set
fruits = ['apple','mango','banana','watermelon','cherry']
print(fruits)
print(fruits[0])

# change value of list using index
fruits[0] = 'pineapple'
print(fruits)

#list slicing
print(fruits[0:3])

#list methods
numbers = [13,10,7,31]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(23)
print(numbers)
numbers.insert(2,35)
print(numbers)
numbers.pop(2)
print(numbers)
numbers.remove(31)
print(numbers)
