#1 :if
a=30
b=200
if b>a:
    print("a is greater")

#2 : if-else
x=30
y=35
if a>b:
    print("a is greater ")
else:
    print("b is greater")


#3 :if-elif-else
c=2
d=3
if c>d:
    print("c is greater")
elif d==c:
    print("d is greater")
else:
    print("not found")

#4 shorthand if
e=100
f=20
if e>f : print("e is greater")

#5 shorthand if-else
g=2
h=10
print("g is greater") if g > h else print("h is greater")

#6 and operator
a=200
b=20
c=10
if a>b and b>c:
    print("both conditions are true")

#7
print("------------------ or operator ---------------:")
x=10
y=20
z=50
if a>b or z>y:
    print("atleast one condition is true ")

#8
print("------------- nested if else --------------- :")
x=15
if x>10:
    print("above 10")
    if(x>20):
        print("above 20 also")
    else:
        print("but not above 20")