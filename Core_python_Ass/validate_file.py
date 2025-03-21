import re

def validation_name(name):
    """Validate that name contains only alphabets"""
    return name if name.isalpha() else " "
    
    

def validate_contact_no(contact_no):
    """validate that contact_no contains only 10 digit"""
    return contact_no if re.fullmatch(r"\d{10}",contact_no) else " "
         
