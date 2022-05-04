# # for x in range(0, 151):
# #     print(x)

# # for x in range(5, 1001):
# #     if x % 5 == 0:
# #         print(x)

# # for x in range(1, 101):
# #     if x % 10 == 0:
# #         print("coding dojo")
# #     elif x % 5 == 0:
# #         print("dojo")
# #     else:
# #         print(x)

# sum = 0
# for x in range(1, 500000, 2):
#     sum += x
# print(sum)

# # for x in range(2018, 0, -4):
# #     print(x)

# low = 2
# high = 9
# mult = 3
# for x in range(low, high+1):
#     if x % mult == 0:
#         print(x)


# def iterateDictionary2(list):
#     for x in list:
#         for key
#         p


# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# iterateDictionary2(students)


from typing import Dict


def analysis(list):
    max = list[0]
    min = list[0]
    sum = 0
    dict = {}
    for i in range(len(list)):
        sum += list[i]
        dict["sum_total"] = sum
        aver = sum/len(list)
        dict['average'] = aver
        if max < list[i]:
            max = list[i]
            dict['maxamium'] = list[i]
        if min > list[i]:
            min = list[i]
            dict['minumam'] = min

    dict["length"] = len(list)
    return dict


a = analysis([2, 37, 1, -9])
print(a)
