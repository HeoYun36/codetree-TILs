n = int(input())

students =[
    tuple(input().split()) for _ in range(n)
]

students.sort(lambda x: (-int(x[1]), -int(x[2]), -int(x[3])))

for student in students:
    print(student[0], student[1], student[2], student[3])

