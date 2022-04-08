# This script was made to test out the agent's functions
import agent
import group
import matplotlib.pyplot as plt



goal = [10, 10]
agentNum = 5
agents = []
for i in range(10):
    if i == 0:
        agents.append(agent.Agent(id=i,leaderflag=True))
    else:
        agents.append(agent.Agent(id=i,leader=agents[0],locx=i,sight=50))

squad = group.Group(agents=agents,goalx=goal[0],goaly=goal[1],avoidance=.2)


for j in range(30):
    squad.update()
    for agent in agents:
        print(agent.id, "-----> Xpos:",agent.x,"Ypos:",agent.y,"Orientation:",agent.orientation,"Speed:",agent.speed)
    print("Iteration #",j)




plt.show()


