#14) Write a Python program to show multilevel inheritance
class Animal:       #grandparent class
    def show(self):
        print("All Animal looks beautiful!!")

class Dog(Animal):      #parent class(inherites from  class Animal)
    def bark(self):
        print("Dog barks")

class Puppy(Dog):       # child class(inherites from Dog class)
    def weep(self):
        print("Puppy weeps")

#creating an object of Puppy
p1 = Puppy()
p1.show()       #inherited from Animal
p1.bark()       #inherited from Dog
p1.weep()       #own method