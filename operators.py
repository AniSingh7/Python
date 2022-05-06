#arithmetic operators
print("arithmetic operators")
x=5
y=3
print(x+y) #addition
print(x-y) #subtraction
print(x*y) # multiplication
print(x/y) # division
print(x%y) # modulus
print(x**y) # exponentiation
print(x//y) #floor division

#Assignment operators
print("Assignment operators")
x=10
y=7
print(x)
print(y)
x+=y
print(x)
x-=y
print(x)
x*=y
print(x)
x/=y
print(x)
x%=y
print(x)
x//=y
print(x)
x**=y
print(x)

#Comparison operators
print("comparison operators")
x=20
y=10
print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

print(id(x))
print(id)
x=10
y=10
print(id(x))
print(id(y))
x=20
print(id(x))

#logical operators
print("logical operators")
x=10
y=10
print(x>=y and x==y)
print(x>y or x==y)
print(not(x>y))

#Identity operator
print("identity operator")
x=10
y=10
print(x==y)
print(x is y)

#Membership operators
print("membership operators")
x=[1,2,3,4,5,6,7]
print(2 in x)


#comparing values
x=10
y=10
print( "values comparison", x==y, x, y)
# comparing address
print("address comparison", x is y , id(x), id(y))
print(x)
#del(x)
print("x value is ", x)
print(x is not y)

#membership
print("membership operator")
y=[2,"x",'y',2.5]
print(2.5 not in y)
print('x' in y)



