#def keyword is used to create a function
def getPercentage(marks):
    return (sum(marks)/500)*100

#directly make use of function/method
marks1 = [45,45,46,45,44]
m1 = getPercentage(marks1)
print(m1)

marks2 = [95,95,76,55,84]
m2 = getPercentage(marks2)
print(m2)

marks3 = [75,75,76,65,64]
m3 = getPercentage(marks3)
print(m3)
