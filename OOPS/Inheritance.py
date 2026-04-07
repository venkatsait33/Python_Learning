# 🔹 Concept
# One class inherits properties from another

class Person: #parent
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print(f"Name: {self.name}")
        
# 🔹 Inheritance, in the Employee class, we are inheriting the properties of the Person class
# 🔹 The Employee class is a subclass of the Person class

class Employee(Person): #child
    def __init__(self, name, salary):
        
        #super() is a special function that allows us to call the constructor of the parent class
        
        super().__init__(name)
        self.salary = salary

    def display(self):
        print(f"Salary: {self.salary}")

emp = Employee("John", 50000)
emp.show()
emp.display()
