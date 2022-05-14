

list_of_tuples=[(1, 2), (2, 3), (3, 4)]
print("The original list of tuples : " + str(list_of_tuples))

res=[list(ele) for ele in list_of_tuples]
print("The converted list of list : " + str(res))


print("common items from two lists")

list1 = [5, 10, 15, 20, 25, 30]
list2 = [10, 20, 30, 40, 50, 60]
common_list = [x for x in list1 if x in list2]
print(common_list)