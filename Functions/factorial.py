n=int(input("enter the number : "))


def factorial(num):
    result = 1
    for i in range(num,0,-1):
        result=result*i
    return result


print("factorial of ", n , "is: " ,factorial(n))