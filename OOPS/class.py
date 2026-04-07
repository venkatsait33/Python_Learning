# Concept
# A class is a blueprint
# An object is a real instance of that blueprint

#creating class
class student:
    # def is a function
    # __init__ is a constructor method
    # self is a reference to the current instance of the class and is used to access variables that belongs to the class
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

#creating Objects
s1 = student("user1", 100)
s2 = student("user2", 200)

s1.display()
s2.display()
