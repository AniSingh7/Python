list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]

def cloning(list):
    list2=list[:]
    return list2


ls=cloning(list1)
print("before cloning: ",list1)
print("after cloning: " ,ls)

