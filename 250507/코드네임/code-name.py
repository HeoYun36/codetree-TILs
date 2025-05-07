class agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []

for _ in range(5):
    codename, score = tuple(input().split())
    agents.append(agent(codename, int(score)))

idx = 0
min_score = agents[0].score

for i in range(1, 5):
    if min_score > agents[i].score:
        min_score = agents[i].score
        idx = i

print(agents[idx].codename, agents[idx].score)
