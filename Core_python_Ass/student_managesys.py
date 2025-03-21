#Write a program to demonstrate the student management system.
from counsellor import add_student , remove_student , view_all_student , view_specific_student
from faculty import add_marks , view_student


while True:
    message = """*************Student Management System*****************
                Press 1 for Counsellor
                Press 2 for Faculty 
                Press 3 for Student
                """
    print(message)

    choice = int(input("Enter a role id : "))

    #select one of below option by counsellor that operation they want to performed
   
    if choice == 1:
            while True:
                detail =""" 
                        1. Add student
                        2. Remove student
                        3. View all student
                        4. View Specific student
                        5. Exits to the application
                        """
                print(detail)

                choice1 = int(input("Enter a choice by counsellor : "))
                if choice1 == 1:
                    add_student()

                elif choice1 == 2:
                    remove_student()

                elif choice1 == 3:
                    view_all_student()

                elif choice1 == 4 :
                    view_specific_student()

                elif choice1 == 5:
                    print("Exits to the application!!!")

                else:
                    print("Invalid choice by counsellor!!!!")

                more_operation = input("Do you want to performed more operation ? (y/n)").lower().strip()
                if more_operation != "y":
                    break
      #select one of below option by counsellorfaculty that operation they want to performed     
    
    elif choice == 2:
          while True:
            mes = """
                    1. Add marks to student
                    2. View all student 
                    3. Exits to the application
                """
            print(mes)
            
            faculty_name = input("Enter faculty name : ").strip()
            choice1 = int(input("Enter a choice by faculty : "))
            if choice1 == 1:
                add_marks(faculty_name)

            elif choice1 == 2:
                view_student(faculty_name)

            elif choice1 == 3:
                print("Faculty exits to the application!!!")

            else:
                print("Invalid choice by faculty!!!!")

            more_operation = input("Faculty can want to perform any othere operation ? (y/n)").lower().strip()
            if more_operation != "y":
                break
    
    elif choice == 3:
        print("Exit the program!!!")
        break

    else:
        print("Invalid choice!!!")







