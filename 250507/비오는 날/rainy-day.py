class Weather:
    def __init__(self, date, day, inf):
        self.date = date
        self.day = day
        self.inf = inf

n = int(input())


weather_data = []

for _ in range(n):
    date, day, inf = tuple(input().split())
    if inf == "Rain":
        weather_data.append(Weather(date, day, inf))


day = weather_data[0].date
idx = 0

for i in range(1, len(weather_data)):
    if day > weather_data[i].date:
        day = weather_data[i].date
        idx = i

print(weather_data[idx].date, weather_data[idx].day, weather_data[idx].inf)
