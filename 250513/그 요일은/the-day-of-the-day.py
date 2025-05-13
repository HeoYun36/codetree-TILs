m1, d1, m2, d2 = map(int, input().split())
day = input()

def f(m, d):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0

    for mon in range(1, m):
        day += months[mon]

    day += d
    
    return day

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

result = 0
interval = f(m2, d2) - f(m1, d1)

result += interval // 7

if day in days[:interval % 7]:
    result +=1

print(result)
