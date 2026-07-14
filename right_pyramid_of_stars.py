#Program to print right pyramid of stars
rows=int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for star in range(1, i + 1):
        print("*", end=" ")
    print()
for j in range(rows - 1, 0, -1):
    for star in range(1, j + 1):
        print("*", end=" ")
    print()