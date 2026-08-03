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
    for star in range(1, i+1):
        print("*", end= "")
    for space in range(1, 2*(num-1)+1):
        print(" ", end="")
    for star in range(1, i+1):
        print("*", end="")
    print()