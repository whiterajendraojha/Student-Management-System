import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change as per your MySQL user
    password="9668263729",  # Change as per your MySQL password
    database="student_management"
)
cursor = db.cursor()

# Functions for CRUD Operations
def add_student(name, age, course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
    db.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if students:
        print("\nID | Name | Age | Course")
        for student in students:
            print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")
    else:
        print("No students found.")

def update_student(student_id, name, age, course):
    cursor.execute("UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s", (name, age, course, student_id))
    db.commit()
    print("Student record updated successfully!")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    db.commit()
    print("Student record deleted successfully!")

# CLI Interface
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")
            add_student(name, age, course)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            course = input("Enter New Course: ")
            update_student(student_id, name, age, course)
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    cursor.close()
    db.close()
