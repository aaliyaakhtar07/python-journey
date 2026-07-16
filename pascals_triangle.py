#Program to print the Pascal's triangle
from math import factorial
rows = int(input("Enter number of rows: "))
for n in range(rows):
    for space in range(rows - n + 1):
        print(end=" ")
    for r in range(n + 1):
        print(factorial(n) // (factorial(r) * factorial(n - r)), end=" ")
    print()