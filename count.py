test_str = "AnishaSinghP"

empty_str = {}

for i in test_str:
    if i in empty_str:
        empty_str[i] += 1
    else:
        empty_str[i] = 1

print ("Count of all characters  is :\n " +  str(empty_str))