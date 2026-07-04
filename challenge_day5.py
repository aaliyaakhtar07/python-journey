'''Complete the code to determine if a person is eligible to drive based on their age and license status.
A person is eligible to drive when:
They are at least 18 years old AND
They have a valid driving license
Fill in the blanks with the correct values:
Fill in the age variable with 20
Fill in the has_license variable with True
Fill in the minimum age requirement in the comparison'''
age = 20
has_license = True
minimum_age = 18
eligible_to_drive = age >= minimum_age and has_license
print(f"Age: {age}, Has License: {has_license}, Eligible to Drive: {eligible_to_drive}")  #Output: Age: 20, Has License: True, Eligible to Drive: True

'''You are given a code. Assign values to x1 and x2 such that x3 evaluates to False.
x1 and x2 should be assigned Boolean values (True or False) or Boolean expressions.'''
x1 = True
x2 = False
x3 = x1 and x2
print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")  #Output: x1 = False, x2 = False, x3 = False