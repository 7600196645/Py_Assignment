# Practical Example 5: Write a Python program to find greater and less than a number using if_else.
'''
num1 = int(input("Enter Number1 : "))
num2 = int(input("Enter Number2 : "))
if num1 <= num2 :
    print(num1 , "is less than", num2)
else:
    print(num2 ,'is greater than', num1)
'''

# Practical Example 6: Write a Python program to check if a number is prime using if_else.
a = int(input("enter number : "))
if a<=1:
    print('not a prime number')
if a%2==0 and a!=2: 
    print(" not a prime number")
elif a%3==0 and a!=3:
    print("not prime no.")
elif a%5==0 and a!=5:    
    print("not prime number")
elif a%7==0 and a!=7 or a%11==0 and a!=11:
    print('Not a Prime number')
else:
    print(a, 'is a prime number')

# Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.

percentage = int(input("Enter a percentage of student : "))
if percentage>=90: 
    print("students have 'Grade A'")
elif percentage>=80: 
    print("students have 'Grade B'")
elif percentage>=70:
    print("students have 'Grade C'") 
elif percentage>=60:
    print("students have 'Grade D'")
else:
    print("students have Failed!")
    
# Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.

age = int(input("Enter a person age: "))
weight = int(input("Enter a person weight: "))
disability = input("is any disability or disease ?\n")
if disability=='No':
    if 18<age<65:
        if weight>45:
            print("Eligible for blood donate")
        else:
            print("Weight is less")
    else:
        print("not in age criteria")
else:
    print("Not Eligible")

