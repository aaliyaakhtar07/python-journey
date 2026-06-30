'''Write a code that initializes three variables, a, b and c with the values 9, 2, and 11 (respectively).
After that, initialize the following variables:
d that will hold the result of a modulo 2 
e that will hold the result of b modulo 3
f that will hold the result of c modulo 10
Check out the result and see how different dividends and divisors affect the result.'''

a = 9
b = 2
c = 11
d = a % 2
e = b % 3
f = c % 10
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}")  

'''Write a code that initializes three variables, x, y and z with the values 15, 4, and 23 (respectively).

After that, initialize the following variables:

w that will hold the remainder of x divided by y  
v that will hold the remainder of z divided by x
u that will hold the remainder of z divided by y
Use the % operator for modulo (remainder).'''
x = 15
y = 4
z = 23
w = x % y
v = z % x
u = z % y
print(f"x = {x}, y = {y}, z = {z}, w = {w}, v = {v}, u = {u}")  