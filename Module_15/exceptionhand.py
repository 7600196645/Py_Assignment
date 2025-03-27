class InvalidInputError(Exception):
    """Raised when the input is not a positive number."""
    pass

try:
    num = int(input("Enter a positive number: "))
    
    if num <= 0:
        raise InvalidInputError("Number must be greater than zero!")

    result = 100 / num
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except InvalidInputError as e:
    print(f"Custom Exception: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program execution completed.")
