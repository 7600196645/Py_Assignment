#20)Write a Python program to show method overriding.
'''Overriding parent class method '''
"""
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a1 = Animal()
a1.speak()

d1 = Dog()
d1.speak()
"""


'''Using super() to call the parent class method'''
"""
class Animal:           #parent class
    def speak(self):
        print("Animal Makes a sound")

class Dog(Animal):          #child class
    def speak(self):        #child class overrides the method but still call the parent method 
        super().speak()     #calling parent class method
        print("Dog barks")

#creating an object
d1 = Dog()
d1.speak()
"""

'''Overriding __init__() constructor''' 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {s1.name}  Age : {s1.age}")

class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)         #call parent constructor
        self.student_id = student_id

    def display(self):
        super().display()       #call parent display method
        print(f"Student_id : {s1.student_id}")

#creating of an object student
s1 = Student("Nisha",26,1605)
s1.display()
        
