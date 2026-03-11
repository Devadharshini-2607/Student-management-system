class Student():
    def __init__(self,Name,Regno,Dept,Year):
        self.Name = Name
        self.Regno = Regno
        self.Dept = Dept
        self.Year = Year

students = []

def add_student():
    Name = input("Enter student name: ")
    Regno = input("Enter reg number: ")
    Dept = input("Enter dept: ")
    Year = input("Enter year: ")

    student = Student(Name,Regno,Dept,Year)
    students.append(student)

    print("Student added successfully")


def view_students():
    if len(students) == 0:
        print("No students found")
    else:
        print("\nStudent List")
        for x in students:
         print("\nName:", x.Name)
         print("Regno:", x.Regno)
         print("Dept:", x.Dept)
         print("Year:", x.Year)


def search_student():
    Regno = input("Enter Register number to search: ")

    for x in students:
        if x.Regno == Regno:
            print("Student found:")
            for x in students:
             print("\nName:", x.Name)
             print("Regno:", x.Regno)
             print("Dept:", x.Dept)
             print("Year:", x.Year)
            return

    print("Student not found")


def delete_student():
    Regno = input("Enter Register number to delete: ")

    for x in students:
        if x.Regno == Regno:
            students.remove(x)
            print("Student deleted")
            return

    print("Student not found")

while True:

    print("\nStudent Management System")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Delete Student")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice")