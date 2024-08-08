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

print(f"name {infos[n - 1].name}")
print(f"addr {infos[n - 1].address}")
print(f"city {infos[n - 1].region}")