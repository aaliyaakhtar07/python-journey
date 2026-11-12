class Employee:
    language = "Python"
    salary = 300000

    def getInfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}.")

    def greet(self):
        print("Hello, welcome to the company!")

aaliya = Employee()
aaliya.language = "JavaScript"
aaliya.greet()
aaliya.getInfo() # or Employee.getInfo(aaliya)