# str1 = "The quick brown fox jumps over the lazy dog."
# print(str1.split(' '))

words="the quick brown fox jumps over the lazy dog"

separted=words.split(' ')
print(separted)

# list1=[]
# for i in separted:
#     list1.append([i,[len(name) for name in separted]])
# print(list1)


# [len(name) for name in separted]
new = [[w.upper(), len(w)] for w in separted]
print(new)