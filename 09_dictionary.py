#dictionary is set of key value pair
userDict = {
    'user_id': 1,
    'name': 'ranveer yadav',
    'email_id': 'yadavranveerp@gmail.com',
    'password': 'pythonworld',
    'marks': [75,78,84], #list
    'subjects': { #nested dictionary
        'primary': 'Maths',
        'secondary': 'English',
        'tertiary': 'Hindi'
    }
}

print(userDict)
print(userDict['email_id'])
print(userDict['name'])
print(userDict['marks'])
print(userDict['subjects'])
print(userDict['subjects']['primary'])

userCool = {
    'user_id': 2,
    'name': 'jivika yadav',
    'name': 'jivika ranveer yadav',
    'email_id': 'yadavjivikar@gmail.com',
    'password': 'ai'
}

print(userCool)
print(userCool['name'])

#methods of dictionary
print(userDict.keys())
print(userDict.values())
print(userDict.items())
print(userDict.get('userId'))
# print(userDict['userId'])
print(userDict.items())
print(list(userDict.keys()))
print(list(userDict.values()))