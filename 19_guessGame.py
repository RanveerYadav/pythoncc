import random
randNumber = random.randint(1,5)

userInput = int(input('Please enter a number'))

if userInput == randNumber:
    print(f'You have guessed the number right {userInput}')
else:
    print('You have guessed wrong number')

