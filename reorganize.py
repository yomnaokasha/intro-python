# sum = 0
# for x in range(1, 500000, 2):
#     sum += x
# print(sum)


# def findEmployee(first_name, list):
#     for employee in list:
#         if employee['first_name'] == first_name:
#             return employee


# employees = [
#     {'first_name': 'Yomna', 'age': 15},
#     {'first_name': 'Mostafa', 'age': 16},
#     {'first_name': 'Hamada', 'age': 18},
# ]


# def convertListToDict(list, key_name):
#     dic = {}
#     # TODO: tomorrow for entry in list:
#     return dic


# employees2 = {
#     'Mostafa': {'first_name': 'Mostafa', 'age': 16},
#     'Yomna': {'first_name': 'Yomna', 'age': 15},
# }

# print('HERE WE GOOOO:', findEmployee('Yomna', employees))
# print('HERE WE GOOOO 2:', employees2['Yomna'])
# 14
# def countdown():
#     emptylist = []
#     for x in range(5, -1, -1):
#         emptylist.append(x)
#     return emptylist


# newlist = countdown()
# print(newlist)


def findodd():
    sum = 0
    for i in range(1, 256, 2):
        sum += i
        print(sum)


findodd()
