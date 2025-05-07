class Secret:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time


code, point, time = input().split()

secret1 = Secret(code, point, time)

print(f'secret code : {secret1.code}')
print(f'meeting point : {secret1.point}')
print(f'time : {secret1.time}')