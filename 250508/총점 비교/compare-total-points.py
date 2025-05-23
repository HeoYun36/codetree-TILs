class Student:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

n = int(input())
students = []

for _ in range(n):
    name, s1, s2, s3 = tuple(input().split())
    students.append(Student(name, s1, s2, s3))

students.sort(key=lambda x: int(x.s1) + int(x.s2) + int(x.s3))

for student in students:
    print(student.name, student.s1, student.s2, student.s3)

