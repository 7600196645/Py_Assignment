#reading a file (r mode)
# file = open("text.txt","r")
# print(file.read())
# file.close()

#Reading file line by line
# file = open("text.txt","r")
# print(file.readline())  #only one line read in the file
# file.close()

#read whole file line by line using loop
# file = open("text.txt","r")
# for line in file:
#     print(line.strip())
# file.close()

#writing to a file
# file = open("text.txt","w") #create or override the file
# file.write("Hello!!! \nPython Programming")
# file.close()

#appending to a file
# file = open("text.txt","a")
# file.write("Adding new line in file\n")
# file.close()

#reading and writing mode(r+ mode)
# file = open("text.txt","r+")
# print(file.read())
# file.write("\nNew content added\n")
# file.close()

#writing and reading mode(w+ mode)
# file = open("text.txt","w+")
# file.write("this is writing and reading mode. It is W+ mode!!!!")
# file.seek(0)
# print(file.read())
# file.close()

#append and read mode(a+ mode)
file = open("text.txt","a+")
file.write("\nThis is append and reading mode.It is a+ mode\n")
file.seek(0)
print(file.read())
file.close()
