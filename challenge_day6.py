'''Replace the values of variables b1 and b2 with numbers so that b3 evaluates to True.
b3 will be True when the multiplication of b1 and b2 is greater than their addition.'''
b1 = 3
b2 = 4
b3 = (b1 * b2) > (b1 + b2)
print(f"b1 = {b1}, b2 = {b2}, b3 = {b3}")  #Output: b1 = 3, b2 = 4, b3 = True

'''Replace the values of variables a, b, and c with boolean values (True or False) so that result evaluates to True.
result will be True when the expression (a or b) and not c is true. Use the logical operators or, and, and not to solve this challenge.'''
a = True
b = False   
c = False
result = (a or b) and not c
print(f"a = {a}, b = {b}, c = {c}, result = {result}")  #Output: a = True, b = False, c = False, result = True


