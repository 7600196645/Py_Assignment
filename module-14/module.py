# 23) Write a Python program to demonstrate the use of functions from the math module. 
import math

print(math.acos(math.radians(30)))
print(math.ceil(5.1))   #Rounds of given value
print(math.comb(10,5))
print(math.sqrt(16))
print(math.degrees(36))
print(math.factorial(6))


# 24) Write a Python program to generate random numbers between 1 and 100 using the random module.
import random
r = random.randint(1,100)
print(r)