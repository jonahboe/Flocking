import math

class Group:
    def __init__(self, pg, screen, agents, followdistance=1, goalx=0, goaly=0, maxspeed=5, avoidance=0.1):
        self.agents = pg.sprite.Group(agents)
        self.screen = screen
        self.followDistance = followdistance  # sets how close this agent should follow its leader
        self.goalx = goalx  # sets what the goal location is
        self.goaly = goaly  # sets what the goal location is
        self.maxSpeed = maxspeed  # sets the max speed of the agent
        self.avoidance = avoidance  # sets how strongly agents will avoid each other

    def update(self):
        convergenceConst = 1
        for agent in self.agents:
            if not agent.leaderFlag:  # check to see if leader the agent is a leader
                tempx = 0  # these variables accumulate the vectors from the leader and nearby agents
                tempy = 0
                if agent.leader is not None:
                    for otherAgent in self.agents:
                        if agent.leader is not otherAgent:
                            if math.sqrt((otherAgent.x - agent.x) ** 2 + (otherAgent.y - agent.y) ** 2) < self.followDistance:  # if an other agent is too close
                                tempx = tempx + (otherAgent.x - agent.x) * self.avoidance  # add a vector with a magnitude based on how close the agent is
                                tempy = tempy + (otherAgent.y - agent.y) * self.avoidance
                        else:
                            if not math.sqrt((otherAgent.x - agent.x) ** 2 + (otherAgent.y - agent.y) ** 2) > agent.sight:  # if the leader is within the agent's sight
                                tempx = tempx + (otherAgent.x - agent.x)
                                tempy = tempy + (otherAgent.y - agent.y)
                            else:
                                agent.leader = None
                                print("Agent",agent.id,"has lost sight of its leader")

                    agent.orientation = ((math.atan2(tempy,tempx) * 180) / math.pi)  # save the new orientation
                    distanceFromLeader = math.sqrt((tempx) ** 2 + (tempy) ** 2)  # calculate the distance the agent is from its leaders
                    convergentSpeed = agent.leader.speed + 1 - math.exp(-((distanceFromLeader - self.followDistance) ** 2) / (convergenceConst ** 2))  # calculate what the speed should be based on how far away the agent is
                    agent.speed = convergentSpeed  # save the new speed
                else:
                    print("WARNING! - Agent", agent.id, "doesn't have a leader")
            else:  # if the agent is the leader
                agent.orientation = ((math.atan2(self.goaly - agent.y, self.goalx - agent.x) * 180) / math.pi)
                distance = math.sqrt((self.goalx - agent.x) ** 2 + (self.goaly - agent.y) ** 2)
                convergentSpeed = 1 - math.exp(-((distance - self.followDistance) ** 2) / (convergenceConst ** 2))
                agent.speed = convergentSpeed

        self.agents.update()  # have agents update
        self.agents.draw(self.screen)
