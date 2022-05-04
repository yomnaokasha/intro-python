# def change_postive(mylist):
#     for i in range(len(mylist)):
#         if mylist[i] > 0:
#             mylist[i] = "big"
#     return mylist


# x = change_postive([-1, 3, 5, -5])
# print(x)


# def replace(mylist):
#     count = 0
#     for i in range(len(mylist)):
#         if mylist[i] > 0:
#             count += 1
#     mylist[-1] = count
#     print(mylist)


# replace([-1, 1, 1, 1])
# replace([1, 6, -2, -7, -2, -4])


# def sum(mylist):
#     sum = 0
#     for i in range(len(mylist)):
#         sum += mylist[i]
#     print(sum)


# sum([1, 2, 3, 4])
# sum([6, 3, -2])


# def average(mylist):
#     sum = 0
#     for i in range(len(mylist)):
#         sum += mylist[i]
#     average = sum / len(mylist)
#     print(average)


# average([1, 2, 3, 4])


# def length(mylist):
#     z = 0
#     for i in mylist:
#         z += 1
#     return z


# x = length([])
# print(x)
# y = length([37, 2, 1, -9])
# print(y)


def mini(mylist):
    lowest = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] < lowest:
            lowest = mylist[i]
    return lowest


x = mini([37, 1, 2, -9])
print(x)
