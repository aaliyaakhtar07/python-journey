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

'''You're helping a weather app determine suitable outdoor activities based on weather conditions. Create a program that uses logical operations to determine if certain activities are possible.

Initialize the following variables:

is_sunny with the value True
temperature with the value 25
wind_speed with the value 10
water_temperature with the value 22
Write the following logical expressions to determine if:

can_go_hiking: It's sunny AND temperature is above 15°C AND wind speed is below 20 km/h
can_go_swimming: It's sunny AND temperature is above 20°C AND water temperature is above 18°C
cannot_go_outside: It's NOT sunny OR temperature is below 10°C OR wind speed is above 30 km/h'''
is_sunny = True
temperature = 25    
wind_speed = 10
water_temperature = 22
can_go_hiking = is_sunny and temperature > 15 and wind_speed < 20
can_go_swimming = is_sunny and temperature > 20 and water_temperature > 18
cannot_go_outside = not is_sunny or temperature < 10 or wind_speed > 30
print(f"Can go hiking: {can_go_hiking}")
print(f"Can go swimming: {can_go_swimming}")
print(f"Cannot go outside: {cannot_go_outside}")
