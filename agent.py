import math

class Agent:
    def __init__(self, id, locx=0, locy=0, leaderflag=False, orientation=0, speed=1, leader=None, sight=5):
        self.id = id
        self.x = locx  # x position
        self.y = locy  # y position
        self.leaderFlag = leaderflag  # indicates if this agent is a leader or not
        self.orientation = orientation  # what direction the agent is facing (degrees)
        self.speed = speed  # how fast the agent is moving in its given direction (m/s)
        self.leader = leader  # sets this agents leader
        self.sight = sight  # sets how far the agent can see

    def move(self):  # assumes 1 sec has passed since last move
        rad = (self.orientation / 180) * math.pi  # convert orientation into radians
        self.x = self.x + math.cos(rad) * self.speed  # update x position
        self.y = self.y + math.sin(rad) * self.speed  # update y position




