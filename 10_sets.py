#set is set of value
#set is collection of non-repetitive element
numbers = {1, 3, 5, 7, 1, 9}
print(numbers)
print(type(numbers))

#empty collection will be treated as an empty dictionary and not empty set
a = {}
print(a)
print(type(a))

#to create empty set
b = set()
print(b)
print(type(b))
b.add(3)
b.add(4)
b.add(5)
b.add((6, 7, 8)) #we can add only tuple in set and not list/dict
print(b)
