#Write a Python program to show multiple inheritance.
class Father:           #one parent class
    def show_father(self):
        print("He is father")

class Mother:           #second parent class
    def show_mother(self):
        print("She is mother")

class Child(Father,Mother):    #child class(inherites from both parent class Father and Mother)
    def show_child(self):
        print("I am a child")

#creating an object of Child
c1 = Child()
c1.show_father()
c1.show_mother()
c1.show_child()
