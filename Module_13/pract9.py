# Write a Python program to demonstrate string slicing.
'''
text = "Hello, Python!"

# Slicing examples
print("Original String :", text)
print("First 5 characters :", text[:5])  # Slice from start to index 4
print("Last 6 characters :", text[-6:])  # Slice the last 6 characters
print("Characters from index 2 to 8 :", text[2:9])  # Slice from index 2 to 8
print("Characters from index 3 to 9 :", text[-12:-4])   #slice from 3 to 9 using negative index
print("Every second character :", text[::2])  # Print every alternate character
print("every 3rd character between index 2 to 6 :", text[2:6:3])
print("Reversed String :", text[::-1])  # Reverse the string
'''

# Write a Python program that manipulates and prints strings using various string methods
text = "Welcome To Python Program!"
message = 'Hello,\tGood\tMorning'
print(len(text))
print(text.capitalize())
print(text.center(50,"*"))
print(text.count("o",2,12))
print(text.endswith("am"))
print(message.expandtabs(10))
print(text.find("m"))
print(text.find("m",6,15))
print(text.index("o"))
print(text.isalnum())
print(text.join(["hii","guys","hello"]))
print(text.ljust(30,"@"))