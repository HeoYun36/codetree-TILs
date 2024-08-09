class info:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

infos = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    infos.append(info(a, b, i + 1))

infos.sort(key= lambda x: (-x.height, -x.weight, x.num))

for people in infos:
    print(people.height, people.weight, people.num)