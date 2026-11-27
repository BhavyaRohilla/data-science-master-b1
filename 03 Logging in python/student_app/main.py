
import logging

# 1. Logging Configuration
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

# 2. Student Database
students = {}

# 3. Add Student
def add_student():

    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")

        if student_id in students:
            logging.warning("Duplicate student ID: %s", student_id)
            print("Student already exists!")
            return

        if not name.strip():
            logging.warning("Empty student name entered")
            print("Name cannot be empty!")
            return

        students[student_id] = name

        logging.info("Student added: ID=%s, Name=%s", student_id, name)
        print("Student added successfully!")

    except ValueError:
        logging.exception("Invalid student ID entered")
        print("Please enter a valid numeric ID!")

# 4. View Students
def view_students():

    if not students:
        logging.warning("No students available")
        print("No records found!")
        return

    for student_id, name in students.items():
        print(f"ID: {student_id} | Name: {name}")

    logging.info("Student records viewed")

# 5. Search Student
def search_student():

    try:
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            logging.info("Student found: ID=%s", student_id)
            print("Student Name:", students[student_id])

        else:
            logging.warning("Student not found: ID=%s", student_id)
            print("Student not found!")

    except ValueError:
        logging.exception("Invalid ID during student search")
        print("Enter a valid numeric ID!")

# 6. Main Application
def main():

    logging.info("Student Management Application started")

    while True:

        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            logging.info("Application closed")
            print("Goodbye!")
            break

        else:
            logging.warning("Invalid menu choice: %s", choice)
            print("Invalid choice!")

if __name__ == "__main__":
    main()
