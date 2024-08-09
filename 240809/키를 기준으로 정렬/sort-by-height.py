class info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

infos = []
for _ in range(n):
    a, b, c = input().split()
    infos.append(info(a, int(b), int(c)))

infos.sort(key= lambda x: x.height)

for people in infos:
    print(people.name, people.height, people.weight)