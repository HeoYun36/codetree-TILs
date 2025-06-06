class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())

students =[]

for i in range(n):
    height, weight = tuple(input().split())
    students.append(Student(int(height), int(weight), int(i + 1)))

students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)
