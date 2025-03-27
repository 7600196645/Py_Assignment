#13) Write a Python program to show single inheritance.
class Animal:       #parent class
    def show(self):
        print("All Animals are beautiful!!!")

class Dog(Animal):      #child class(inherites from Animal)
    def bark(self):
        print("Dog barks")

#creating an object of Dog
d1 = Dog()
d1.show()       #inhetited method
d1.bark()       #own method