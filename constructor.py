class Employee:
    language = "Python" #This is a class attribute
    salary = 300000

    def __init__(self, name, salary, language): #Dunder method which is automatically called when an object is created
        self.name = name
        self.salary = salary
        self.language = language
        print("An employee object has been created.")

aaliya = Employee("Aaliya", 300000, "C++")
print(f"The name is {aaliya.name}.\nThe salary is {aaliya.salary}.\nThe language is {aaliya.language}.")