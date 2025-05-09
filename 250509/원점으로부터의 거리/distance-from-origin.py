def f(n):
    if n < 0:
        return -n
    else:
        return n

class Point:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

n = int(input())
points = []

for i in range(n):
    x, y = tuple(map(int, input().split()))
    points.append(Point(x, y, i + 1))


points.sort(key=lambda x: (f(x.x) + f(x.y)))

for point in points:
    print(point.num)




