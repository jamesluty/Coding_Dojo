# 1. Update Values in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ]
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# def update_x(x_list):
#     x_list[1][0] = 15
#     return x_list

# def update_students(dict):
#     dict[0]['last_name'] = 'Bryant'
#     return dict

# def update_sports_directory(sportDict):
#     # tempDict = sportDict['soccer']
#     # tempDict[0] = 'Andres'
#     # sportDict['soccer'] = tempDict

#     sportDict['soccer'] = ['Andres', 'Ronaldo', 'Rooney']
#     return sportDict

# def update_z(z_list):
#     z_list[0]['y'] = 30
#     return z_list

# print(update_x(x))
# print(update_students(students))
# print(update_sports_directory(sports_directory))
# print(update_z(z))




# 2. Iterate Through a List of Dictionaries

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(someList):
#     for listValue in someList:
#         for key, value in listValue.items():
#             print(key, " - ", value)

# iterateDictionary(students) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel




# 3. Get Values From List of Dictionaries

# def iterateDictionary2(name, list):
#     for listValue in list:
#         if name == 'first_name':
#             print(listValue['first_name'])
#         elif name == 'last_name':
#             print(listValue['last_name'])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)




# 4. Iterate Through a Dictionary With List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    firstList = dict['locations']
    secondList = dict['instructors']

    print(str(len(firstList)) + " LOCATIONS")
    for city in firstList:
        print(city)

    print(str(len(secondList)) + "INSTRUCTORS")
    for name in secondList:
        print(name)


printInfo(dojo)
