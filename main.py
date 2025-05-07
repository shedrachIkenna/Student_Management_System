class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name 
        self.student_id = student_id
        self.gpa = gpa 
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student_id: {self.student_id}")
        print(f"GPA: {self.gpa}")
    
    def __str__(self):
        return f"{self.name} | {self.student_id} | {self.gpa}"
    
students_db = []

def create_student():
    name = input("Enter student name: ")
    student_id = int(input("Enter student ID: "))
    gpa = float(input("Enter student GPA: "))

    new_student = Student(name, student_id, gpa)
    students_db.append(new_student)

    print(f"{name} has been successfully added to the system!")

def read_student():
    id = int(input("Enter student ID to view student info: "))
    found = False 
    for student in students_db:
        if student.student_id == id:
            print("\nStudent Found")
            student.display_info()
            found = True 
            break
    if not found:
        print("Student not found\n")

def update_student():
    id = int(input("Enter student ID to update credentials: "))

    for student in students_db:
        if student.student_id == id: 
            print("/nCurrent credentials: ")
            student.display_info()
            print("what would you like to change: ")
            print("1. Name")
            print("2. GPA")
            choice = int(input("Select 1/2: "))
            if choice == 1:
                new_name = input("Enter new name: ")
                student.name = new_name
            elif choice == 2:
                new_gpa = input("Enter new GPA: ")
                student.gpa = new_gpa
            else:
                print("Invalid option!")
                return
            
            print("/nStudent info successfully updated!")
            student.display_info()
            return 
    
    print("Student not found")

def delete_student():
    id = int(input("Enter the student ID you want to delete: "))
    for student in students_db:
        if student.student_id == id:
            confirm = input(f"Are you sure you want to delete {student.name} y/n?:").lower()
            if confirm == "y":
                students_db.remove(student)
                print(f"{student.name} deleted successfully!")
            else:
                print("Deletion cancelled")
            return 
    
    print("Student not found!")

def list_all_students():
    if not students_db:
        print(f"\nStudent not found")
    else: 
        print(f"\nAll Students")
        for student in students_db:
            print(student)

def main():
    while True:
        print("Student Management System")
        print("1. Create Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. List All Students")
        print("6. Exit")

        choice = input("Select and option (1-6): ")
        if choice == "1":
            create_student()
        elif choice == "2":
            read_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5": 
            list_all_students()
        elif choice == "6":
            print("goodbye")
            break 
        else:
            print("Invalid option! Please try again")

main()