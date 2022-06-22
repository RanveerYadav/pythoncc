#both file location indication will work
# fileOpen = open('D:/pythoncc/File to be operated.txt')
# fileOpen = open('File to be operated.txt', 'r') #byfefault mode is r
fileOpen = open('File to be operated.txt') #byfefault mode is r
fileData = fileOpen.read()
print(fileData)
fileOpen.close()


fileOpen = open('File to be operated.txt') #byfefault mode is r
fileData = fileOpen.read(13) #number indicates the character it will read
print(fileData)
fileOpen.close()

fileOpen = open('File to be operated.txt', 'w')
fileOpen.write('Asia Continent')
print(fileOpen)
fileOpen.close()