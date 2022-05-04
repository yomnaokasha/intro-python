x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)


def iterateDictionary(list):
    for entry in list:
        for key, val in entry.items():
            print(key, " - ", val)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students)


def iterateDictionary2(key_name, list):
    for key in list:
        print(key[key_name])


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


def printInfo(some_dict):
    for key, array in some_dict.items():
        print("===========================")
        print(len(array), key)
        for entry in array:
            print(entry)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)


def add(b, c):
    print(b+c)


print(add(1, 2) + add(2, 3))
