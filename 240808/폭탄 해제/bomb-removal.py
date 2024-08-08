class bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time


arr = tuple(input().split())

new_bomb = bomb(arr[0], arr[1], arr[2])

print(f"code : {new_bomb.code}")
print(f"color : {new_bomb.color}")
print(f"second : {new_bomb.time}")