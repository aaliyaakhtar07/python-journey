#Program to print the fibonacci series up to n terms
terms=int(input("Enter the number of terms: "))
n1,n2=0,1
if terms<0:
    print("Please enter a positive integer")
elif terms==1:
    print("Fibonacci sequence up to",terms,"term:")
    print(n1)
else:
    print("Fibonacci sequence up to",terms,"terms:")
    for i in range(terms):
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3