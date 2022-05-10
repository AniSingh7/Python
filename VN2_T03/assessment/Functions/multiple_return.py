# return sum,sub
# 	Output
# 	The Sum is : 150
# 	The Subtraction is : 50

n1 =int(input("enter the number "))
n2=int(input("enter the number "))

def func(n1,n2):
   sum=n1+n2
   sub=n1-n2
   return sum,sub


a,b=func(n1,n2)
print("The Sum is :" , a)
print("The Subtraction is :" , b)


