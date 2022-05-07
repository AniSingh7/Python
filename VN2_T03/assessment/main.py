# L = [11, 33, 50]
#
# out = int("".join(map(str, L)))
# print("exp output:", out)

input = "1234abcd"

def reverse_str(input):
    res = ""
    for i in input:
        res = i + res
    return res

print("After reverse output string:",reverse_str(input))

