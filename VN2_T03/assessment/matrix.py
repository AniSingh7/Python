# 1. adding nest list inside a list
print("'addition of nested list in a list'")

X=[[1,2,3],[4,5,6]]
res=[]

print("The original list is :" + str(X))
for i in range(len(X)):
    res1=X[0]
    res2=X[1]

#print(res1)
#print(res2)
for i in range(0,len(res1)):
    res.append(res1[i]+res2[i])


print("sum of matrix elements is: " + str(res))