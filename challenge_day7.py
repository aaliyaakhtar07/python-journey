'''Write code that checks if a person is eligible to drive. A person is eligible to drive if ALL of the following conditions are met:
The person is at least 18 years old
The person has a license
The person has insurance
The following starter code is already provided for you — it reads the inputs and converts them to the correct types:
age = int(input()) — reads the age as an integer
has_license = input() == "true" — reads the license string and converts it to a boolean
has_insurance = input() == "true" — reads the insurance string and converts it to a boolean
Your task is to:
Check all three conditions using the variables age, has_license, and has_insurance, and store the result in a variable named result'''
age = int(input())
has_license = input() == "true"         
has_insurance = input() == "true"
result = age >= 18 and has_license and has_insurance
print(result)  #Output: True or False depending on the inputs