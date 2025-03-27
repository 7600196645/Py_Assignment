# Practical Examples: 4) Write a Python program to create a file and print the string into the file. 
'''
with open("text2.txt","w+") as file:
     file.write("Good afternonn!!!")
     file.write("\nWelcome to Python Programming")
     print("String has been writtern to file")
    '''

# 5) Write a Python program to read a file and print the data on the console. 
# with open("text2.txt","r") as file:
#      print(file.read())

# 6) Write a Python program to check the current position of the file cursor using tell().
with open("text2.txt","a") as file:
    file.write("\nIndia is my country")
    file.writelines(["My Name is Nisha\n","I am from Bharuch\n"])
    print(file.tell())
