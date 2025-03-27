# 12) Write a Python program to demonstrate the use of local and global variables in a class.
# Global variable
count = 0  

class Example:
    """Demonstrating local and global variables in a class"""
    
    def __init__(self, name):
        self.name = name  # Instance attribute (local to the object)

    def show(self):
        local_var = "I am local to show() method"  # Local variable
        print(f"Inside show() method: {local_var}")
        print(f"Accessing global count inside class (read-only): {count}")
    
    def modify_global(self):
        global count  # Declaring that we want to modify the global variable
        count += 1
        print(f"Modified global count inside class: {count}")

# Creating an object of Example class
obj = Example("Python")

# Accessing local and global variables
obj.show()

# Modifying global variable
obj.modify_global()

#print attrtibute value and modify that value
#print(obj.name)
# obj.name = "Java"
# print(obj.name)

# Checking global variable outside the class
print(f"Global count outside class: {count}")
