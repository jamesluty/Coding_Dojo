def countdown(number):
    numArr = []
    while number >= 0:
        numArr.append(number)
        number -= 1
    return numArr

print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[1]

aList = [5,7]
funReturn = print_and_return(aList)
print(funReturn)

def first_plus_length(list):
    listSum = list[0] + len(list)
    return listSum

bList = [1,2,3,4,5]
print(first_plus_length(bList))

def values_greater_than_second(list):
    newList = []
    if len(list) > 1:
        argNum = list[1]
    else:
        return False

    for num in list:
        if num > argNum:
            newList.append(num)
    return newList

cList = [5,2,3,2,1,4]
dList = [3]
print(values_greater_than_second(cList))
print(values_greater_than_second(dList))

def this_length_that_value(size,value):
    valueList = []
    number = 0
    while number < size:
        valueList.append(value)
        number += 1
    return valueList

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))

