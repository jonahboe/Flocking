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

AGENT_COUNT = 10
FPS = 40
SCREEN_SIZE = 1000
GOAL = [400, 400]
SIGHT = 200

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('Flocking')

if __name__ == '__main__':
    # Set up some data collection
    data = {BORDA: [],
            PLURALITY: [],
            VETO: []}

    # Prompt for user input
    vm = BORDA
    display = True
    cycles = 0
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
                vm = PLURALITY
            if sys.argv[i + 1] == 'v':
                vm = VETO
        elif sys.argv[i] == "-d":
            if sys.argv[i + 1] == 'f':
                display = False
        elif sys.argv[i] == "-c":
            cycles = int(sys.argv[i + 1])

    # Set up the agents
    agents = []
    for i in range(AGENT_COUNT):
        if i == 0:
            agents.append(agent.Agent(pg=pygame, screen=screen, id=i, leader=0, leaderflag=True, locx=(i * 20 + 20), locy=(i * 20 + 20), sight=SIGHT))
        else:
            agents.append(agent.Agent(pg=pygame, screen=screen, id=i, leader=0, locx=(i*20+20), locy=(i*20+20), sight=SIGHT))
    squad = group.Group(pg=pygame, screen=screen, agents=agents, goalx=GOAL[0], goaly=GOAL[1], avoidance=.5, avoiddistance=10, followdistance=10, maxspeed=2, maxturnspeed=5)

    iteration = 0
    running = True
    while running:
        # Fill the background white
        screen.fill(WHITE)

        squad.update(display)
        squad.vote(vm, data, display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(data)
                pygame.quit()

        if display:
            pygame.display.update()
            clock.tick(FPS)

        if cycles > 0:
            if iteration >= cycles:
                print(data)
                sys.exit(0)
            iteration += 1




