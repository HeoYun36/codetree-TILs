n = int(input())
grade = list(map(float, input().split()))

avg = sum(grade) / n
print(f'{avg:.1f}')
if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')