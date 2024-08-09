class scoreboard:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

socre_list = []
n = int(input())
for _ in range(n):
    a, b, c, d = input().split()
    score = scoreboard(a, int(b), int(c), int(d))
    socre_list.append(score)

socre_list.sort(key= lambda x: x.kor + x.eng + x.math)

for people in socre_list:
    print(people.name, people.kor, people.eng, people.math)