list=[1,2,3,4,5]

def mul_list(list):
    mul=1
    for i in list:
        mul=mul*i
    return mul

print("product of list elements is: ", mul_list(list))


tuple=[1,2,3]

def mul_tuple(tuple):
    mul=1
    for i in tuple:
        mul=mul*i
    return mul

print("product of tuple elements is: ", mul_list(tuple))

set={1,4,5}

def mul_set(set):
    mul=1
    for i in set:
        mul=mul*i
    return mul

print("product of set elements is: ", mul_set(set))


