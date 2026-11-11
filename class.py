class Employee:
    language = "Python" #This is a class attribute
    salary = 30000

aaliya = Employee()
print(aaliya.salary)
print(aaliya.language)

rohan = Employee()
rohan.name = "Rohan" #This is an instance attribute
print(rohan.name)
print(rohan.salary)
print(rohan.language)

harry = Employee()
harry.language = "JavaScript"
print(harry.language)
#Here name is object attribute and salary and language are class attributes as they directly belong to the class.