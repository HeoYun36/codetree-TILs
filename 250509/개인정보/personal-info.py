class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

def print_all(people):
    for person in people:
        print(person.name, person.height, person.weight)

people = []

for _ in range(5):
    name, height, weight = input().split()
    people.append(Person(name, int(height), float(weight)))

people.sort(key=lambda x: x.name)

print("name")
print_all(people)

print()

people.sort(key=lambda x: -x.height)

print("height")
print_all(people)
