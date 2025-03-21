# Create a mini-project where students combine conditional statements, loops, and functions to create a basic Python application, such as a simple calculator or a grade management system.
def addition(num1,num2):
    sum = num1 + num2
    return sum

def subtraction(num1,num2):
    subtract = num1 - num2
    return subtract

def multiplication(num1,num2):
    multiply = num1 * num2
    return multiply

def division(num1,num2):
    div = num1 / num2
    return div

def modulus(num1,num2):
    mod = num1 % num2
    return mod

print("select your choice for perform below operation :\n \
        1. Addition\n\
        2. Subtraction\n\
        3. Multiplication\n\
        4. Division\n\
        5. modulus\n")

choice = int(input("Enter your choice : "))
n1 = int(input("Enter number1 : "))
n2 = int(input("Enter Number2 : "))
if choice == 1:
    add = addition(n1,n2)
    print("Addition of two number is : " ,add)

elif choice == 2:
    sub = subtraction(n1,n2)
    print("Subtraction of two number is : ",sub)

elif choice == 3:
    mul = multiplication(n1,n2)
    print("Multiplication of two number is : ", mul)

elif choice == 4:
    divi = division(n1,n2)
    print("Division of two number is : ", divi)

else:
    modu = modulus(n1,n2)
    print("Modulus of two number is : " , modu)