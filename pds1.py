#Patterns in python
'''for i in range(1,6):
    print("*")'''

'''for i in range(1,6):
    print("*", end="")'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print("*")'''

'''for i in range(1,6):
    for j in range(1,6):
        print("*", end="")
    print()'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()'''

'''for i in range(5,0, -1):
    for j in range(1,i+1):
        print('*', end=" ")
    print()'''

'''for i in range(1,6):
    for space in range(1, 6-i):
        print(" ", end=" ")
    for star in range(1,i+1):
        print("*", end=" ")
    print()'''

'''for i in range(5,0,-1):
    for space in range(1, 6-i):
        print(" ", end=" ")
    for star in range(1, i+1):
        print("*", end=" ")
    print()'''

'''for i in range(1,6):
    for space in range(1, 6-i):
        print(" ", end=" ")
    for star in range(1,(2*i-1)+1):
        print("*", end= " ")
    print()'''

num = int(input("Enter a number:"))
for i in range(1, num+1):
    star = "*"*i
    space = " "*(2*(num-i))
    print(star+space+star)
for j in range(num-1, 0, -1):
    star = "*"*j
    space = " "*(2*(num-j))
    print(star+space+star)

