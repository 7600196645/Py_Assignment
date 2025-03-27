# city = input("Which city are you live ? ")
# print(f"I am Lived in {city} ")

# age = int(input("Enter ypur age : ")) 
# print(f"I am {age} years old")

# price = float(input("Enter price of product :"))
# print(f"price of product is {price:.2f}")

#Handling multiple input using split()
x , y = input("Enetr two number for sum : ").split(sep=",")
x , y = int(x),int(y)
print("sum :", x + y)