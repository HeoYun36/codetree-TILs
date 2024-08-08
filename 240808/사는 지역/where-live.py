class info:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

n = int(input())

infos = []
for _ in range(n):
    a, b, c = input().split()
    infos.append(info(a, b, c))

infos.sort(key= lambda x: x.name)

print(f"name {infos[-1].name}")
print(f"addr {infos[-1].address}")
print(f"city {infos[-1].region}")