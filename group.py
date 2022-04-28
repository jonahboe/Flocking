import math
import random

class Group:
    def __init__(self, pg, screen, agents, followdistance=1, goalx=0, goaly=0, maxspeed=5, avoidance=0.15, avoiddistance=10, maxturnspeed=15):
        self.agents = pg.sprite.Group(agents)
        self.screen = screen
        self.followDistance = followdistance  # sets how close this agent should follow its leader
        self.goalx = goalx  # sets what the goal location is
        self.goaly = goaly  # sets what the goal location is
        self.maxSpeed = maxspeed  # sets the max speed of the agent
        self.avoidance = avoidance  # sets how strongly agents will avoid each other
        self.maxTurnSpeed = maxturnspeed  # sets how fast an agent can turn in degress
        self.avoidDistance = avoiddistance

    def update(self):
        convergenceConst = 1
        for agent in self.agents:
            if not agent.leaderFlag:  # check to see if leader the agent is a leader
                tempx = 0  # these variables accumulate the vectors from the leader and nearby agents
                tempy = 0
                if agent.leader is not None:
                    for otherAgent in self.agents:
                        if agent.leader is not otherAgent:
                            dis = math.sqrt((otherAgent.x - agent.x) ** 2 + (otherAgent.y - agent.y) ** 2)
                            if dis < self.avoidDistance:  # if an other agent is too close
                                tempx = tempx + (-otherAgent.x + agent.x) * self.avoidance  # add a vector with a magnitude based on how close the agent is
                                tempy = tempy + (-otherAgent.y + agent.y) * self.avoidance
                        else:
                            dis = math.sqrt((otherAgent.x - agent.x) ** 2 + (otherAgent.y - agent.y) ** 2)
                            if not dis > agent.sight:  # if the leader is within the agent's sight
                                tempx = tempx + (otherAgent.x - agent.x)
                                tempy = tempy + (otherAgent.y - agent.y)
                            else:
                                agent.leader = None
                                print("Agent",agent.id,"has lost sight of its leader")
                                self.agents.update()  # have agents update
                                self.agents.draw(self.screen)
                                return
                    distanceFromLeader = math.sqrt((tempx) ** 2 + (tempy) ** 2)  # calculate the distance the agent is from its leaders
                    if distanceFromLeader - self.followDistance < 0:
                        convergentSpeed = 0
                    else:
                        if distanceFromLeader > self.maxSpeed:
                            convergentSpeed = self.maxSpeed
                        else:
                            convergentSpeed = distanceFromLeader
                    agent.speed = convergentSpeed  # save the new speed
                    if agent.speed != 0:
                        tempO = ((math.atan2(tempy, tempx) * 180) / math.pi)
                        diff = abs(agent.orientation - tempO)
                        if diff > 180:
                            diff = diff - 360
                        elif diff < -180:
                            diff = diff + 360
                        if abs(diff) > self.maxTurnSpeed:
                            diff2 = agent.orientation - tempO
                            if diff2 > 180:
                                diff2 = diff2 - 360
                            elif diff2 < -180:
                                diff2 = diff2 + 360
                            if diff2 > 0:
                                agent.orientation = - self.maxTurnSpeed + agent.orientation
                            else:
                                agent.orientation = self.maxTurnSpeed + agent.orientation
                            if agent.orientation > 180:
                                agent.orientation = agent.orientation - 360
                            if agent.orientation < -180:
                                agent.orientation = agent.orientation + 360
                        else:
                            agent.orientation = tempO  # save the new orientation
                else:
                    print("WARNING! - Agent", agent.id, "doesn't have a leader")
            else:  # if the agent is the leader
                agent.orientation = ((math.atan2(self.goaly - agent.y, self.goalx - agent.x) * 180) / math.pi)
                distance = math.sqrt((self.goalx - agent.x) ** 2 + (self.goaly - agent.y) ** 2)
                convergentSpeed = 1 - math.exp(-((distance - self.followDistance) ** 2) / (convergenceConst ** 2))
                agent.speed = convergentSpeed
                # If we have reached our goal, then generate a new one
                if distance < 15:
                    self.goalx = random.randint(0, 1000)
                    self.goaly = random.randint(0, 1000)

        self.agents.update()  # have agents update
        self.agents.draw(self.screen)

    def vote(self, voting):
        for agent in self.agents:
            if agent.leader is None:
                agentList = [agent]
                voteList = [agent.id]
                for neighbor in self.agents:
                    if neighbor is not agent:
                        dx = abs(agent.x - neighbor.x)
                        dy = abs(agent.y - neighbor.y)
                        if math.sqrt(dx + dy) < agent.sight:
                            agentList.append(neighbor)
                            voteList.append(neighbor.id)
                for agent in agentList:
                    agent.votes = voteList
                leader = voting.process(agentList)
                for agent in agentList:
                    agent.leader = leader
                    if agent.id == leader:
                        agent.leaderFlag = True

