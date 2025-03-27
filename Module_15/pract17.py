# 17) Write a Python program to show hybrid inheritance.
class Animal:           #parent class1
    def show(self):
        print("All animals are beautiful!!!")

class cat:          #parent class2
    def meow(self):
        print("cat sounds Meow")

class Dog(Animal):      #child class(inherites from Animal)
    def bark(self):
        print("dog barks")

class Puppy(Dog,cat):       #Another child class(inherites from Dog and Cat)
    def weep(self):
        print("Puppy weeps")

p1 = Puppy()
p1.show()
p1.meow()
p1.bark()
p1.weep()


