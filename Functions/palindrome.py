# def isPalindrome(s):
#     return s == s[::-1]
#
#
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")


def palindrome(str1):
    if str1 == str1[::-1]:
        print("It is palindrome")
    else:
        print("It is not a palindrome")


str=input("enter a string to check whether it is a palindrome or not :")
palindrome(str)

