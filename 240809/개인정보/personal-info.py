class info:
    def __init__(self, name, heigth, weight):
        self.name = name
        self.heigth = heigth
        self.weight = weight

infos = []
for _ in range(5):
    a, b, c = input().split()
    infos.append(info(a, int(b), float(c)))

infos.sort(key= lambda x: x.name)

print("name")
for people in infos:
    print(people.name, people.heigth, people.weight)

infos.sort(key= lambda x: -x.heigth)

print()

print("height")
for people in infos:
    print(people.name, people.heigth, people.weight)