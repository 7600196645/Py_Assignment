#19)Write a Python program to show method overloading
'''Using Default arguments for method overloading'''
"""
class Calculator:
    def add(self, a, b=0, c=0):  # Default values allow different numbers of arguments
        return a + b + c

# Creating an object
calc = Calculator()

# Calling method with different numbers of arguments
print(calc.add(5))        # Calls add(a), uses default b=0, c=0
print(calc.add(5, 10))    # Calls add(a, b), uses default c=0
print(calc.add(5, 10, 15))  # Calls add(a, b, c)
"""

'''Using *args (Variable Arguments) for Overloading'''
"""
class Calculator:
    def add(self,*args):            #accepts any number of arguments
        return sum(args)

#creating of an object
cal = Calculator()

#calling method with different number of arguments
print(cal.add(5,10,15))
print(cal.add(12,15))
print(cal.add(1,2,4,10,5))
print(cal.add(10))
"""


'''Using Type checking (isinstance()) for method overloading'''
class Printer:
    def display(self,data):
        if isinstance(data,int):
            print("Integer :", data)

        elif isinstance(data,float):
            print("Floating : ", data)

        elif isinstance(data,bool):
            print("Boolean : ", data)

        elif isinstance(data,str):
            print("String :", data)

        elif isinstance(data,list):
            print("List : ", data)

        else:
            print("Unsupported data type")

p1 = Printer()
p1.display("Nisha")
p1.display(10.5)
p1.display("A")
p1.display(0)
p1.display([1,2,3,4,5])
p1.display(True)

