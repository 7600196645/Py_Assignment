# Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.).
# create a list
#l1 = [10,20,35.6,58.0,"Apple","banana",True]

# Write a Python program to access elements at different index positions
# l1 = [10, 20, 35.6, 58.0, "Apple" , "banana" , True]
# print(l1[-1])
# print(l1[3])
# print(l1[2:7])
# print(l1[-6:-2])
# print(l1[::-1])
# print(l1[1:7:3])
# print(l1[1:7:2])
# print(l1[-7::2])
# print(l1[-7:-2:2])

# Write a Python program to create a list of multiple data type elements.
#l1 = [10,20,35.6,58.0,"Apple","banana",True]
# Write a Python program to find the length of a list using the len() function.
# l1 = [10,20,35.6,58.0,"Apple","banana",True]
# print(len(l1))

# Write a Python program to add elements to a list using insert() and append().
'''
l1 = [10,20,35.6,58.0,"Apple","banana",True]
l1.insert(3,"mango")
print(l1)
l1.append(50)
print(l1)
'''

# Write a Python program to remove elements from a list using pop() and remove().
# l1 = [10,20,35.6,58.0,"Apple","banana",True]
# l1.pop()    #by default at element remove at end.
# print(l1)
# l1.pop(3)   #remove element from specific index
# print(l1)
# l1.remove(35.6)
# print(l1)

# Write a Python program to iterate over a list using a for loop.
'''
l1 = ["apple", "banana",10,20,23.6]
for i in l1:
    print(i)
'''

# Write a Python program to sort a list using both sort() and sorted().
'''
l1 = [10,20,23.6,4,10,6]
l1.sort()
print(l1)
l2 = sorted(l1)
print(l2)
'''

# Pract 6 : Write a Python program to insert elements into an empty list using a for loop and append().
city = []
for i in range(1,6):
    name = input("enter city name : ")
    city.append(name)
print(city)
