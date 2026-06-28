a=10
b=20
#Assignment operators are used to assign values to variables.
c=a+b  # c is assigned the value of a + b
print("Value of c:", c)  # Output: Value of c: 30
a+=5  # a is incremented by 5, equivalent to a = a + 5
print("Value of a:", a)  # Output: Value of a: 15
a-=3  # a is decremented by 3, equivalent to a = a - 3
print("Value of a:", a)  # Output: Value of a: 12
b*=2  # b is multiplied by 2, equivalent to b = b *2
print("Value of b:", b)  # Output: Value of b: 40
b/=4  # b is divided by 4, equivalent to b = b / 4
print("Value of b:", b)  # Output: Value of b: 10.0     
b%=3  # b is assigned the remainder of b divided by 3, equivalent to b = b % 3
print("Value of b:", b)  # Output: Value of b: 1.0
b**=2  # b is raised to the power of 2, equivalent to b = b ** 2
print("Value of b:", b)  # Output: Value of b: 1.0
b//=2  # b is floor divided by 2, equivalent to b = b // 2
print("Value of b:", b)  # Output: Value of b: 0.0
a&=2  # a is bitwise ANDed with 2, equivalent to a = a & 2
print("Value of a:", a)  # Output: Value of a: 0
a|=3  # a is bitwise ORed with 3, equivalent to a = a | 3
print("Value of a:", a)  # Output: Value of a: 3
a^=1  # a is bitwise XORed with 1, equivalent to a = a ^ 1
print("Value of a:", a)  # Output: Value of a: 2
a<<=1  # a is left shifted by 1, equivalent to a = a << 1
print("Value of a:", a)  # Output: Value of a: 4
a>>=1  # a is right shifted by 1, equivalent to a = a >> 1
print("Value of a:", a)  # Output: Value of a: 2
#Membership opertors are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary). The two membership operators in Python are in and not in.
list1 = [1, 2, 3, 4, 5]
print(3 in list1)  # Output: True
print(6 not in list1)  # Output: True