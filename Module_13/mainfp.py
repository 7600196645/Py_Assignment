# Write a Python program to apply the map() function to square a list of numbers.
'''
l1 = [1,5,6,8,9,11,20,25]
square_list = list(map(lambda x : x * x , l1))
print("square of list  : ", square_list)
'''

# Write a Python program that uses reduce() to find the product of a list of numbers.
'''
from functools import reduce
l1 = [1,5,6,8,9,11,20,25]
producr_list = reduce(lambda  x , y : x * y, l1)
print("Product of list : " , producr_list)
'''

# Write a Python program that filters out even numbers using the filter() function.
l1 = [1,5,6,8,9,11,20,25]
even_list = list(filter(lambda x : x % 2 == 0, l1))
print("event number in list  : ", even_list)
