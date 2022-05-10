a = {}
n = int(input("Enter number of elements:"))
for i in range(n):
    k = input("Enter key:")
    v = input("Enter value:")
    a.update({k:v})
print(a)