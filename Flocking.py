"""
Demonstrates the use of different voting mechanisms as solutions to the leader election problem, in association with
flocking algorithms.

By:
    Jonah Boe
    Rhett Redd
    Matthew Shaw

CS-5110, Utah State University
Spring, 2022
"""
import sys
import agent
import group
import pygame
from voting import *

AGENT_COUNT = 20
FPS = 40
SCREEN_SIZE = 1000
GOAL = [400, 400]

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('Flocking')

if __name__ == '__main__':
    # Take the user input
    # Prompt for user input
    voting = Borda()
    for i in range(len(sys.argv)):
        print(sys.argv[i])
        if sys.argv[i] == "-h":
            print("-h: Print help (this list of commands) and exit.")
            print("-v: Set voting mechanism. b(default): borda, p: plurality, v: veto")
            sys.exit(0)
        elif sys.argv[i] == "-v":
            if sys.argv[i + 1] == 'b':
                break
            if sys.argv[i + 1] == 'p':
                voting = Plurality()
            if sys.argv[i + 1] == 'v':
                voting = Veto()

    # Set up the agents
    agents = []
    for i in range(AGENT_COUNT):
        if i == 0:
            agents.append(agent.Agent(pg=pygame, screen=screen, id=i, leaderflag=True, locx=400, locy=200))
        else:
            agents.append(agent.Agent(pg=pygame, screen=screen, id=i, leader=agents[0], locx=(i*20+200), locy=(i*20+200), sight=500))
    squad = group.Group(pg=pygame, screen=screen, agents=agents, goalx=GOAL[0], goaly=GOAL[1], avoidance=.5, avoiddistance=10, followdistance=10, maxspeed=2, maxturnspeed=5)

    x = 0
    running = True
    while running:
        # Fill the background white
        screen.fill(WHITE)

        squad.update()
        # for agent in agents:
        #      print(agent.id, "-----> Xpos:", agent.x, "Ypos:", agent.y, "Orientation:", agent.orientation, "Speed:", agent.speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        clock.tick(FPS)


