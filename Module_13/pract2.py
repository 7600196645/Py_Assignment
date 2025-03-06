# Write a Python program that demonstrates the correct use of indentation, comments, and variables following PEP 8 guidelines.
'''  Calculate the Area and Perimeter of a Rectangle '''
# This program prompts the user for the length and width of a rectangle, calculates the area and perimeter, and displays the results.
        
# Program to calculate the area and perimeter of a rectangle
'''
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The calculated area.
    """
    return length * width

def calculate_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The calculated perimeter.
    """
    return 2 * (length + width)

    # Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

    # Calculate area and perimeter
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

    # Display the results
print(f"\nRectangle Dimensions: {length} x {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
'''
