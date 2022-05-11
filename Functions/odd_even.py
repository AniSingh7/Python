num=int(input("enter the number to check whether it is odd or even? "))

def check(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

print(check(num))