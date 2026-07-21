#Program to count the number of digits, letters, and special characters
s = input("Enter a string: ")
d, l, o = 0, 0, 0
for c in s:
    if c.isdigit():
        d += 1
    elif c.isalpha():
        l += 1
    else:
        o += 1
print("Digits:", d)
print("Letters:", l)
print("Special characters:", o)