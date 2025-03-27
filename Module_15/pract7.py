#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
# Practical Examples: 7) Write a Python program to handle exceptions in a calculator. 

def calculator():
    try:
        num1 = int(input("Enter number1 : "))
        num2 = int(input("Enter number2 : "))

        result = num1/num2
        print(f"Result of {num1}/{num2} = {result}")

    except ZeroDivisionError as e:
        print("Error : Division by 0 is not allowed")

    except ValueError as e :
        print("Error : Invalid Input!! plz enter numeric value")

    except Exception as e:
        print(f"An unexpected error occured {e}")

calculator()





