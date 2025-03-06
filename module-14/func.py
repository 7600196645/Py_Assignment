# 19) Write a Python program to print a string using a function. 
'''
def print_text(msg):
    print(msg)

s1 = input("Enter String :")
print_text(s1)
'''

# 20) Write a Python program to create a parameterized function that takes two arguments and prints their sum. 
'''
def sum(num1,num2):
    return num1 + num2

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
add = sum(n1,n2)
print(add)
'''

# 21) Write a Python program to create a lambda function with one expression. 
'''
square = lambda x : x * x 
print(square(5))
'''

# 22) Write a Python program to create a lambda function with two expressions.
multi_expression = lambda x : (x * x, x + x)
print(multi_expression(20))