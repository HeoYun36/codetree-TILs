class agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agents = []
for _ in range(5):
    agent_name, agent_score = input().split()
    agents.append(agent(agent_name, int(agent_score)))

agents.sort(key=lambda x: x.score)

print(f"{agents[0].name} {agents[0].score}")