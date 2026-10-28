n = int(input("Enter the number for table: "))
print("Multiplication table")
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
print()
print("Reverse multiplication table")
#Reverse multiplication table
for i in range(10, 0, -1):
    print(f"{n} X {i} = {n*i}")