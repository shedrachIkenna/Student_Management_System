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


create_student()
read_student()

print("All the students in the system")
for student in students_db:
    print(student)