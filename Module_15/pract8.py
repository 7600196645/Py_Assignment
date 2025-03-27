# 8)Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

def multiple_exceptions():
    try:
        # File Handling (Trying to open a non-existing file)
        # with open("test.txt", "r") as file:
        #     content = file.read()
        #     print(f"File Content: {content}")

        # Taking input from the user
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        # Performing division
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

    except FileNotFoundError:
        print("Error: The file was not found!")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
multiple_exceptions()


# 9) Write a Python program to handle file exceptions and use the finally block for closing the file. 
def read_file():
    try:
        # File Handling (Trying to open a non-existing file)
        with open("text.txt", "r") as file:
             content = file.read()
             print(f"File Content: {content}")


    except FileNotFoundError:
        print("Error: The file was not found!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        try:
            file.close()
            print("file closed successfully!!!")

        except NameError as e :
            print("File was never opened so no need to closed")

# Run the function
read_file()