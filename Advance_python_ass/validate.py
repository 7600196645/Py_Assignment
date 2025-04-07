import re

def validate_name(name):
        if name.isalpha():
            return name
        
        else:
            print("invalid name !!!enter only alphabets!!!")
            name = input("Enter username : ")

def validate_contact_no(contact_no):
    pattern = r"^\d{10}$"
    while True:
        if re.match(pattern,contact_no):
            return contact_no
        else:
            print("Invalid contact_no!!!Enter only 10 digit number")
            contact_no = input("Enter contact_no : ")

def validate_email(mail_id):
    #pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    pattern = r"^[a-zA-Z0-9._%+-]+@+gmail+\.[a-zA-Z]{2,}$"
    while True:
        if re.match(pattern,mail_id):
            return mail_id
        else:
            print("Invalid mail id!!")
            mail_id = input("Enter mail id : ")