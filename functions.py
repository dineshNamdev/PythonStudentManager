students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    student = {"name": name, "Student_id": student_id}
    students.append(student)

def save_file(student):
    try:
        f = open("student.txt","a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not save files")

def read_file():
    try:
        f = open("student.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("could not read files")

read_file()
print_students_titlecase()

student_name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")

add_student(student_name, student_id)
save_file(student_name)

