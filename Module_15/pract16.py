#16) Write a Python program to show hierarchical inheritance. 
class Animal:       #parent class
    def show(self):
        print("All animals are beautiful!!!")

class Dog(Animal):      #one child class(inhetires from Animal)
    def bark(self):
        print("Dog barks")

class Cat(Animal):      #secong chihld class(inherites from Animal)
    def meow(self):
        print("cat meows!!")
#creating an object of Dog and Cat
d1 = Dog()
c1 = Cat()

d1.show()
d1.bark()

c1.show()
c1.meow()
