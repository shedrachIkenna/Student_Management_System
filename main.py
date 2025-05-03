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
    id = int(input("Enter student ID"))
    found = False 
    for student in students_db:
        if student.student_id == id:
            print("\nStudebt Found")
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
            print("what would you like to change")
            print("1. Name")
            print("2. GPA")
            choice = int(input("Select 1/2"))
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


create_student()
read_student()
update_student()

print("All the students in the system")
for student in students_db:
    print(student)