import re
#from validate_file import validation_name , validate_contact_no
from log_manager import log_transaction

student_data = {}
def add_student():
    
    #stored already enter sr_no
    enter_sr_no  = set()
    num = int(input("Enter the number of student want to add by counsellor  : "))

    for i in range(1,num + 1):
    
          #to check duplicate sr_no
          while True:
               sr_no = int(input("\nEnter a Serial Number : "))
               if sr_no in enter_sr_no:
                print(f"{sr_no} is already exists!!!Plz enter a unique sr_no .")
               else:
                enter_sr_no.add(sr_no)
                break

          """apply validation to first name and last name"""
          while True:      
               # fname = validation_name(input("Enter a First Name : ").strip())
               # lname = validation_name(input("Enter a Last Name : ").strip())
               fname = input("Enter a First Name : ").strip()
               lname = input("Enter a Last Name : ").strip()
               if fname.isalpha() and lname.isalpha():
                    break
               else:
                    print(input("Invalid name!!!Plz Enter only alphabetical character "))
          
          '''apply validation to contact no'''
          while True:          
               #contact_no = validate_contact_no(input("Enter a Contact Number : ").strip())
               contact_no = input("Enter a Contact Number : ").strip()
               if re.fullmatch(r"\d{10}",contact_no):
                    break
               else:
                    print("Invalid contact number!!!Plz Enter only 10 digit number ")

          #create nested dictory for subject
          subjects = {}

          while True:
                 subject = input("Enter subject name  : ")
                 mark = int(input("Enter subject mark : "))
                 fees = int(input("Enter subject fees : "))

                 subjects[subject] = {"marks": mark , "fees" : fees}

                 more_subject = input("want to Add another subject? (y/n)").strip().lower()
                 if more_subject != "y":
                      break
            
          faculty = input("Enter Faculty name : ").strip()

          student_data[sr_no] = {"fname" : fname , "lname" : lname , "contact_no" : contact_no , "subject" : subjects , "faculty" : faculty }
          print(student_data)
          log_transaction(f"Student {fname} {lname} added successfully")
          print("student added successfully")


#remove student 
def remove_student():
    """Remove student by id with confirmation"""
    sr_no = int(input("Enter student id to remove : ").strip())

    if sr_no in student_data:
         confirm_mes = input("Are you sure to remove student ? (y/n) : ").strip().lower()
         
         if confirm_mes == "y":
              del student_data[sr_no]
              log_transaction(f"student {sr_no} removed successfully")
              print("Student removed successfully")

         else:
              print("remove operation cancelled.!!")

    else:
         print("Student_id not found!!")


#display all student information
def view_all_student():
    """Display all student details"""
    if not student_data:
         print("No student found")

    else:
          for sr_no , details in student_data.items():
                       print(f"{sr_no} : {details}")


#display specific  student information fetch by sr_no
def view_specific_student():
    """Display specific student details"""
    sr_no = int(input("Enter student_id to show their details : ").strip())

    if sr_no in student_data:
         print(student_data[sr_no])

    else:
         print("Invalid student id !!!")


            
           