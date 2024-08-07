class message:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time


a, b, c = input().split()

a = message(a, b, c)

print(f'secret code : {a.code}')
print(f'meeting point : {a.place}')
print(f'time : {a.time}')