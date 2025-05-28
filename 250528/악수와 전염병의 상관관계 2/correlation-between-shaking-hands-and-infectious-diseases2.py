N, K, P, T = map(int ,input().split())

# 전염병 여부와 남은 전염 횟수를 저장
timeline = []
dev_arr = [{"disease": "off", "count": K} for _ in range(N + 1)]

dev_arr[P]["disease"] = "on"

for i in range(T):
    t, x, y = map(int, input().split())
    timeline.append([t, x, y])

timeline.sort(lambda x: x[0])

for inf in timeline:
    x = inf[1]
    y = inf[2]

    if dev_arr[x]["disease"] == "on" and dev_arr[y]["disease"] != "on":
        if dev_arr[x]["count"] > 0:
            dev_arr[x]["count"] -= 1
            dev_arr[y]["disease"] = "on"
    elif dev_arr[x]["disease"] != "on" and dev_arr[y]["disease"] == "on":
        if dev_arr[y]["count"] > 0:
            dev_arr[y]["count"] -= 1
            dev_arr[x]["disease"] = "on"
    elif dev_arr[x]["disease"] == "on" and dev_arr[y]["disease"] == "on":
        if dev_arr[x]["count"] > 0 or dev_arr[y]["count"] > 0:
            dev_arr[x]["count"] -= 1
            dev_arr[y]["count"] -= 1

for i in range(1, len(dev_arr)):
    if dev_arr[i]["disease"] == "on":
        print(1, end='')
    else:
        print(0, end='')

            
            

    

