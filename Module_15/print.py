#Write a Python program to print a formatted string using print() and f-string
# print("Hello, World")
# print("Hello", "Bharuch" ,"Good Mornig!!!",sep=",")  #printing multiple values
# print("Hello",end="!!!")    #changing end character
name = "Nisha"
print("Name :",name )   #printing variable value


# Using f-string
# pi = 3.14159
# print(f"Pi to 2 decimal places :{pi:.2f}")

# name = "Alice"
# age = 25
# print(f"My name is {name} and my age is {age}")

# number = 20
# print(f"Left alignment {number : >10}") #adding padding
# print(f"Right alignment {number : <10}")

# a , b = 10 , 20
# print(f"Sum of {a} and {b} is : {a + b}")

#Using format()
name = "Ninsha"
place = "Bharuch"
print("My name is {} and i am from {}".format(name,place))

pi = 3.14159265358
print("Pi to 3 decimal is {:.3f}".format(pi))

number = 40
print("Left alignmrnt : {:>10}".format(number))