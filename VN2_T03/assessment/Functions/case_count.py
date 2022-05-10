str1=input("enter a string :")


def count(str1):
    uc = 0
    lc = 0
    for i in str1:
        if i.isupper():
            uc = uc + 1
        elif i.islower():
            lc = lc + 1
    return uc,lc



upper_count,lower_count=count(str1)

print("count of upperCase is:",upper_count)
print("count of lowerCase is:",lower_count)