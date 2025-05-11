class Student:
    def __init__(self, height, weihgt, num):
        self.height = height
        self.weight = weight
        self.num = num

n = int(input())

students = []

for i in range(n):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight, i + 1))

students.sort(key= lambda x: (x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.num)