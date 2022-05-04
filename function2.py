def countdown():
    emptylist = []
    for x in range(5, -1, -1):
        emptylist.append(x)
    return emptylist


newlist = countdown()
print(newlist)


def print_and_return(mylist):
    print(mylist[0])
    return mylist[1]


x = print_and_return([1, 2])
print(x)


def first_plus_length(list):
    sum = list[0] + len(list)
    return sum


y = first_plus_length([1, 2, 3, 4, 5])
print(y)


def values_greater_than_second(list):
    if len(list) < 2:
        return False
    newlist = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            newlist.append(list[i])
    print(len(newlist))
    return(newlist)


x = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(x)


y = values_greater_than_second([1])
print(y)


def length_and_value(size, value):
    newlist = []
    for i in range(0, size):
        newlist.append(value)
    return newlist


print(length_and_value(4, 7))
print(length_and_value(6, 2))


def length_and_value(size, value):
    empty_list = []
    for x in range(size):
        empty_list.append(value)
    return empty_list


a = length_and_value(4, 7)
b = length_and_value(6, 2)
print(a)
print(b)
