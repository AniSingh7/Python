
list=[1,4,2,3,5,1,4,6,7,5,1,7]

def unique_ele(list1):
    unique_list=[]
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(unique_ele(list))
