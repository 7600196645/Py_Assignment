# Write a Python program to open a file in write mode, write some text, and then close it.
# writing to a file
file = open("text.txt","w") #create or override the file
file.write("Hello!!! \nPython Programming")
file.close()

# Practical Example: 3) Write a Python program to create a file and write a string into it.
file = open("text.txt","w") #create or override the file
file.write("Hello!!! \nGood morning!!!\n")
file.close()
