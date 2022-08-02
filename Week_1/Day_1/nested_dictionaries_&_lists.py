#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x[1][0])
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students[0]['last_name'])
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory['soccer'][0])
# Change the value 20 in z to 30
z[0]["y"] = 30
print(z[0]["y"])

#2 Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#Create a function that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
# def iterateDictionary(students):
#     for i in range(0, len(students)):
#         dict = students[i]
#         for key, val in dict.items():
#             print(key + " - " + val)

# iterateDictionary(students)

##BONUS## 
def iterateDictionary(students):
    for i in range(0, len(students)):
        dict = students[i]
        first_name = dict['first_name']
        last_name = dict['last_name']
        print("first_name - " + first_name + ", last_name - " + last_name)
iterateDictionary(students)

#3 Get Values From a List of Dictionaries
# Create a function that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
def iterateDictionary2(key, students):
    for i in range(0, len(students)):
        print(students[i][key])

iterateDictionary2('last_name', students)
iterateDictionary2('first_name', students)

#4 Iterate Through a Dictionary with List Values
# Create a function that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print(str(len(dojo['locations'])) + " LOCATIONS")
    for location in dojo['locations']:
        print(location)
    print(str(len(dojo['instructors'])) + " INSTRUCTORS")
    for instructors in dojo['instructors']:
        print(instructors)
printInfo(dojo)
