#Write a Python program to insert data into an SQLite3 database and fetch it.
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("my_database.db")

# Create a cursor object
cursor = conn.cursor()

# Function to insert data
def insert_user(name, age, email):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
    cursor.execute(query, (name, age, email))
    conn.commit()
    print("User added successfully!")

# Function to fetch all users
def fetch_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("\nUser List:")
    for user in users:
        print(user)

# Insert some data
insert_user("nisha", 25, "npatel@gmail.com")
insert_user("megha", 30, "mp@gmail.com.com")

# Fetch and display all users
fetch_users()

# Close the connection
conn.close()
