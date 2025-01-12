class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


john = Student("john", list(map(float, input().split("; "))))

num_students = int(input())

better_students = []

for i in range(1, num_students + 1):
    student_data = input().split(": ")
    student = Student(student_data[0], list(map(float, student_data[1].split(", "))))

    if student.average() > john.average():
        better_students.append(f"{i}) {student.name}")

if better_students:
    for student in better_students:
        print(student)
else:
    print("None of the students performed better")
