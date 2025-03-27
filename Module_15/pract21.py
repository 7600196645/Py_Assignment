#Write a Python program to create a database and a table using SQLite3.
import sqlite3

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("my_database.db")

# Create a cursor object
cursor = conn.cursor()

# SQL query to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE NOT NULL
);
"""

# Execute the query
cursor.execute(create_table_query)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
