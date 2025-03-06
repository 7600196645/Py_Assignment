# 13) Write a Python program to create a dictionary of 6 key-value pairs.
'''
d = {"Name" : "Nisha",
     "Lname" : "Patel",
     "age" : 25,
     "city" : "Ahmedabad",
     "gender" : "Female",
     "mark" : 78.65
     }

print(d)
'''

# 14) Write a Python program to access values using keys from a dictionary.
'''
d = {"Name" : "Nisha",
     "Lname" : "Patel",
     "age" : 25,
     "city" : "Ahmedabad",
     "gender" : "Female",
     "mark" : 78.65
     }

print(d["age"])
print(d["Lname"])
print(d["Name"])
'''

# 15) Write a Python program to update a value at a particular key in a dictionary. 
'''
d = {"Name" : "Nisha",
     "Lname" : "Patel",
     "age" : 25,
     "city" : "Ahmedabad",
     "gender" : "Female",
     "mark" : 78.65
     }
d["mark"]= 80

print(d)
'''

# 16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods. 
'''
d = {"Name" : "Nisha",
     "Lname" : "Patel",
     "age" : 25,
     "city" : "Ahmedabad",
     "gender" : "Female",
     "mark" : 78.65}

print(d.keys())
print(d.values())
'''

# 17) Write a Python program to convert two lists into one dictionary using a for loop.
'''
d = {}
number = [1,2,3,4,5,6]
square = [1,4,9,16,25,36]
for i in range(len(number)):
    d[number[i]]=square[i]
print(d)
'''
#using zip() 
'''
d = {}
number = [1,2,3,4,5,6]
square = [1,4,9,16,25,36]

for number,square in zip(number,square):
    d[number]=square
print(d)
'''

# 18) Write a Python program to count how many times each character appears in a string.
'''
d ={}
text = input("Enter Text : ")
for i in text:
    d[i]=d.get(i,0)+1
print(d)
'''
'''
from collections import Counter
d = {}
text = input("Enter text : ")
d = Counter(text)

print(d)
'''