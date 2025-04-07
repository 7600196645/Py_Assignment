#This is Database connection file
import pymysql
#class Database:
       
        # def __init__(self):
            
        #     try:
        #         print("initialize")
        #         self.conn = mysql.connector.connect(
        #         host = 'localhost',
        #         user = 'root',
        #         password = '',
        #         database = 'pharmacy_db',
                
        #      )
        #         self.cursor = self.conn.cursor()   
        #         print("database connected successfully")  
        #     except mysql.connector.Error as err:
        #         print(f"Error {err}")
        #         self.conn = None

mydb = pymysql.connect(host='localhost',user='root',password='')
mycursor = mydb.cursor()

mycursor.execute('create database if not exists pharmacy_management')
mydb.commit()

mydb = pymysql.connect(host='localhost',user='root',password='',database='pharmacy_management')
mycursor = mydb.cursor()

mycursor.execute('create table if not exists admin (id int auto_increment primary key,name varchar(100),password varchar(100),contact_no varchar(10),mail_id varchar(100))')
mydb.commit

mycursor.execute('create table if not exists pharmacy_manager (id int auto_increment primary key,name varchar(100) not null,password varchar(100) not null,contact_no varchar(10),mail_id varchar(100),phrmacy_name varchar(100) not null)')
mydb.commit()

mycursor.execute('create table if not exists medicine (id int auto_increment primary key,medicine_name varchar(200),quantity int not null,add_data varchar(100) not null,added_by varchar(20),price int)')
mydb.commit()

def close_fun():
    if mycursor.close() and mydb.close():
        print("database connection close successfully")
    else:
        print("database connection not close !!!")