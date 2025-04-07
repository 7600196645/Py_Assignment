#Write a program to demonstrate the application pharmacy management system 
try:
     
     import database_py
     from database_py import close_fun
     from user import Admin,Pharmacy_Manager
     #print("module import successfullly")

except ImportError as e:
     print("Import error : ",e)

try:
     
     if database_py.mydb:
    
         print("database initialize successfully")
     else:
         print("database connection failed")
         exit()
except Exception as e:
     print("Error during database initialization  :",e)
     exit()



while True:
    menu = """
        **************Pharmacy Management System***************
                        1. Admin
                        2. Pharmacy Manager 
                        3. Exits to the application       
        """
    print(menu)
    choice = int(input("Enter a choice : "))
    
    if choice == 1:
             
             while True:
                 admin_menu = """
                         1. Register
                         2. Login
                         3. View all Manager
                         4. View all Medicine
                         5. Exit to the application
                     """
                 print(admin_menu)
            
                 admin_option  = int(input("Enter choice by Admin : ").strip())
                 admin = Admin()
                 if admin_option == 1:
                    admin.register()

                 elif admin_option == 2:
                     admin.login()
                     

                 elif admin_option == 3:
                     admin.view_all_manager()

                 elif admin_option == 4:
                     admin.view_all_medicine() 

                 elif admin_option == 5:
                     print("Admin Exits to the application!!!")
                     break

                 else:
                     print("Invalid choice by admin!!!Plz choose valid option!!!")

                 admin_mes = input("Do you want to perform any other operation by Admin ?(y/n)  ").lower().strip()
                 if admin_mes != 'y':
                     break

    elif choice == 2:
             ph_manager = Pharmacy_Manager()
             while True:
                 ph_manager_menu = """
                             1. Register
                             2. Login
                             3. Add Medicine
                             4. View Medicine
                             5. Delete Medicine
                             6. Exit to the application
                     """
                 print(ph_manager_menu)
                 ph_manager_option = int(input("Enter a option choose by pharmacy manager : "))
                 if ph_manager_option == 1:
                     ph_manager.register()

                 elif ph_manager_option == 2:
                     ph_manager.login()

                 elif ph_manager_option == 3:
                     ph_manager.add_medicine()

                 elif ph_manager_option == 4:
                     ph_manager.view_medicine()

                 elif ph_manager_option == 5:
                     ph_manager.delete_medicine()

                 elif ph_manager_option == 6:
                     print("pharmacy manager exit to the application!!!")
                     break
                
                 else:
                     print("Invalid choice by pharmacy manager!!!Plz enter valid option!!!")

                 ph_manager_mes = input("Do you want to perform any other operation by pharmacy manager ? (y/n)  ").lower().strip()
                 if ph_manager_mes != 'y':
                      break
    
    elif choice == 3:
         print("Exits to the appliocation!!!")
         break
    else:
         print("invalid choice!!!")




