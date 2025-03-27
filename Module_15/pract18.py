#18) Write a Python program to demonstrate the use of super() in inheritance
class Car:                      #parent class
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def display_show(self):
        print(f"car name : {t1.name} \ncar brand : {t1.model}")

class Tata(Car):            #child class
    def __init__(self, name, model,colour):
        super().__init__(name, model)           #calling parent class constructor
        self.colour = colour

    def display_show(self):
        super().display_show()          #calling parent class method
        print(f"car colour : {t1.colour}")
#creating an object of Tata
t1 = Tata("Nexon","sepy 300","Red")
t1.display_show()
