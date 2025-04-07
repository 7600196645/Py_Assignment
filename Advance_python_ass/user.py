
import database_py
from validate import validate_contact_no,validate_email,validate_name
from tabulate import tabulate


     

class Admin():
    """class Admin for admin"""

    def register(self):
            """Registers as a Admin"""
            self.username = validate_name(input("Enter  username : ").strip())
            self.fullname = input("Enter fullname : ").strip()
            self.contact_no = validate_contact_no(input("Enter contact number : ").strip())
            self.mail_id = validate_email(input("Enter mail id : ").strip())
       
            while True:
                self.password = input("Enter password : ").strip()
                self.confirm_pass = input("Enter confirm password : ").strip()

                if self.password == self.confirm_pass:
                      break
                    
                else:
                    print("password & confirmed password are mismatched!!!")

            
            query = "INSERT INTO admin (name,password,contact_no,mail_id) VALUES (%s,%s,%s,%s)"
            database_py.mycursor.execute(query,(self.username,self.password,self.contact_no,self.mail_id))
      
            database_py.mydb.commit()
            print(f"{self.username} Registered successfully!!!")
                        


    def login(self):
      """Login as Admin"""
      while True:
            username = validate_name(input("Enter name : "))
            password = input("Enter password : ")
            query = "SELECT *FROM admin WHERE name = %s AND password = %s"
            database_py.mycursor.execute(query,(username,password))
            
        
            result = database_py.mycursor.fetchone()
            database_py.mydb.commit()
            if result:
                  print(f"{username} login successfully")
                  break
                  
            else:
                  print("Invalid username or password")

   
    def view_all_manager(self):
        """Admin can view all manager"""
        query = "SELECT id,name,pharmacy_name FROM pharmacy_manager"
        database_py.mycursor.execute(query)
        managers = database_py.mycursor.fetchall()
        database_py.mydb.commit()
        
        header = ["Id", "Name", "Pharmacy_Name"]

        if managers:
             print(tabulate(managers,headers=header,tablefmt="grid"))

        else:
              print("no manager found")
              

    def view_all_medicine(self):
          '''Admin can view all medicine details'''
          query = "SELECT id,medicine_name,quantity,add_date,added_by,price FROM medicine"
          database_py.mycursor.execute(query)
          medicines = database_py.mycursor.fetchall()
          database_py.mydb.commit()

          header = ["Id", "Medicine Name",  "Quantity", "Add Date", "Added By", "Price"]

          if medicines:
               print(tabulate(medicines,headers=header,tablefmt="grid"))

          else:
                print("no medicine found")


          
class Pharmacy_Manager():
    """class for pharmacy manager"""
            
    def register(self):
      """Registers as a Pharmacy manageruser"""
      self.username = validate_name(input("Enter  username : ").strip())
      self.fullname = input("Enter fullname : ").strip()
      self.contact_no = validate_contact_no(input("Enter contact number : ").strip())
      self.mail_id = validate_email(input("Enter mail id : ").strip())
      self.pharmacy_name = input("Enter manager pharmacy name : ").strip()

      while True:
                self.password = input("Enter password : ").strip()
                self.confirm_pass = input("Enter confirm password : ").strip()

                if self.password == self.confirm_pass:
                      break
                    
                else:
                    print("password & confirmed password are mismatched!!!")
      query = "INSERT INTO pharmacy_manager (name,contact_no,mail_id,password,pharmacy_name) VALUES (%s,%s,%s,%s,%s)"
      database_py.mycursor.execute(query,(self.username,self.contact_no,self.mail_id,self.password,self.pharmacy_name))
      database_py.mydb.commit()
      print(f"{self.username} Registered successfully!!!")

    
    def login(self):
      """Login as Pharmacy manager"""
      while True:
            username = validate_name(input("Enter name : "))
            password = input("Enter password : ")
            query = "SELECT *FROM pharmacy_manager WHERE name = %s AND password = %s"
            database_py.mycursor.execute(query,(username,password))
            manager_result = database_py.mycursor.fetchone()
            database_py.mydb.commit()

            if manager_result:
                  print(f"{username} loging successfully!!!")
                  break
            else:
             print("Invalid username!!")


    def add_medicine(self):
          """Add a medicine details """
          while True:
            self.manager_name = input("Enter username : ").strip()
            query = "SELECT *FROM pharmacy_manager WHERE name = %s"
            if database_py.mycursor.execute(query,(self.manager_name)):
               break
            else:
              print("Invalid username!!! ") 

          self.medicine_name = input("Enter Medicine name : ").strip()
          self.__qty = int(input("Enter medicine quantity : "))
          self.add_date = input("Enter medicine date : ")
          self.add_by = input("Enter added by : ").strip()
          self.price = int(input("Enter medicine price : "))

          query = "INSERT INTO medicine (ph_manager_name,medicine_name,quantity,add_date,added_by,price) VALUES (%s,%s,%s,%s,%s,%s)"
          database_py.mycursor.execute(query,(self.manager_name,self.medicine_name,int(self.__qty),self.add_date,self.add_by,int(self.price)))
          database_py.mydb.commit()
          print(f"{self.medicine_name} added successfully")
          
    
    def view_medicine(self):
          """View all medicines details"""
          self.manager_name = input("Enter pharmacy nameger name :")
          query = "SELECT id,medicine_name,quantity,add_date,added_by,price FROM medicine WHERE ph_manager_name = %s"
          database_py.mycursor.execute(query,(self.manager_name))
          medicines = database_py.mycursor.fetchone()
          database_py.mydb.commit()

          header = ["Id", "Manager Name",  "Quantity", "Add Date", "Added By", "Price","Medicine Name"]
          if medicines:
                  print(tabulate([medicines],headers=header,tablefmt="grid"))

          else:
                print("no medicine found")

    
    def delete_medicine(self):
          """Delete a medicine"""
          medicine_name = input("Enter medicine name to delete : ").strip()
          msg = input("Are you sure you want to delete medicine ? (y/n)  ").lower().strip()
          if msg == 'y':
            query = "DELETE FROM medicine WHERE medicine_name = %s"
            database_py.mycursor.execute(query,(medicine_name))
            database_py.mydb.commit()
            print(f"{medicine_name} deleted successfully")



    

