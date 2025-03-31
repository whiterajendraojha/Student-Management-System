import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change as per your MySQL user
    password=""   # Change as per your MySQL password
)
cursor = db.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_management")
cursor.execute("USE student_management")

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(255) NOT NULL
);
""")

db.commit()
cursor.close()
db.close()
