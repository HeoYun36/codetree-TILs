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


day = int(weather_data[0].date[:4])
idx = 0

for i in range(1, len(weather_data)):
    if day > int(weather_data[i].date[:4]):
        day = int(weather_data[i].date[:4])
        idx = i

print(weather_data[idx].date, weather_data[idx].day, weather_data[idx].inf)
