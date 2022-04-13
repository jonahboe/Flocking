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
import agent
import group
import pygame

AGENT_COUNT = 1
FPS = 40
SCREEN_SIZE = 1000
GOAL = [100, 400]

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('Flocking')

# Set up the agents
agents = []
for i in range(AGENT_COUNT):
    if i == 0:
        agents.append(agent.Agent(pg=pygame, screen=screen, id=i, leaderflag=True))
    else:
        agents.append(agent.Agent(pg=pygame, screen=screen, id=i, leader=agents[0], locx=i, sight=50))
squad = group.Group(pg=pygame, screen=screen, agents=agents, goalx=GOAL[0], goaly=GOAL[1], avoidance=.2)

x = 0
running = True
while running:
    # Fill the background white
    screen.fill(WHITE)

    squad.update()
    for agent in agents:
        print(agent.id, "-----> Xpos:", agent.x, "Ypos:", agent.y, "Orientation:", agent.orientation, "Speed:", agent.speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    clock.tick(FPS)


