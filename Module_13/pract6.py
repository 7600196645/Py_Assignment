# Write a generator function that generates the first 10 even numbers.
'''
def even_number():
    num = 2
    count = 0
    while count < 10:
        yield num
        num +=2
        count += 1

for even in even_number():
    print(even)
'''

# Write a Python program that uses a custom iterator to iterate over a list of integers.

class ListIterator:
    def __init__(self,number):
        self.number =number
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.number):
            raise StopIteration
        value = self.number[self.index]
        self.index +=1
        return value
    
num_list = [10,20,30,40,50,60,70,80,90,100]
iterator = ListIterator(num_list)

for num in iterator:
    print(num)

        