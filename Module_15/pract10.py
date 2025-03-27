# 10) Write a Python program to print custom exceptions.
# Define a custom exception class
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    def __init__(self, value, message="Negative numbers are not allowed!"):
        self.value = value
        self.message = message
        super().__init__(self.message)

# Function to check if a number is positive
def check_positive_number(num):
    try:
        if num < 0:
            raise NegativeNumberError(num)  # Raising the custom exception
        print(f"Valid input: {num} is a positive number.")
    
    except NegativeNumberError as e:
        print(f"Custom Exception: {e.message} (Entered: {e.value})")

# Taking user input
try:
    number = int(input("Enter a positive number: "))
    check_positive_number(number)
except ValueError:
    print("Error: Invalid input! Please enter an integer.")

