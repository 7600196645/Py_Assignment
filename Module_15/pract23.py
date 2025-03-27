#23) Write a Python program to search for a word in a string using re.search(). 
import re

text = "Hello guys!! Welcome to Python Programming!!!"

search_word = re.search(r"guys",text)

if search_word:
    print("word found at index : " , search_word.start())

else:
    print("Word not found!!")

#24) Write a Python program to match a word in a string using re.match().
import re

text = "Welcome to Python Programming class!!!"

match_word = re.match("Welcome",text)

if match_word:
    print("match found in text", match_word.group())

else:
    print("match not found")

