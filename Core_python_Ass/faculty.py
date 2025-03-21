from log_manager import log_transaction
from counsellor import student_data

def add_marks(faculty_name):
    """Faculty can add marks only to assigned student"""
    sr_no = int(input("Enter student_id : ").strip())

    #to check if student exist or not
    if sr_no in student_data:
        #verify faculty name
        if student_data[sr_no]["faculty"] != faculty_name:
            print("\n Access denied!!!you can only modified your assigned student!!")

        subjects = input("Enter subject name to update marks : ").strip()

        if subjects in student_data[sr_no]["subject"]:
            new_marks = int(input("Enter new marks : ").strip())
            student_data[sr_no]["subject"][subjects]["marks"] = new_marks
            log_transaction(f"marks updated for student {sr_no} in {subjects}")
            print("marks updated successfully!!!")

        else:
            print("Subject not found for this student!!!")

    else:
        print("student not found!!!Invalid student id")

#function for faculty to view their own student details
def view_student(faculty_name):
    """Faculty can view assigned student"""
    #faculty_name = input("Enter faculty name : ").strip()
    found = False
    
    for sr_no , details in student_data.items():
        if details["faculty"] == faculty_name:
            found = True
            print(f"{sr_no}: {details}")
            
    if not found:
            print("No student assigned to tis faculty!!!")

    