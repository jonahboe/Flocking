import math
import pygame
import random


class Agent(pygame.sprite.Sprite):
    def __init__(self, pg, screen, id, locx=0, locy=0, leaderflag=False, orientation=0, speed=1, leader=None, sight=5,
                 *groups):
        # Initialize our agent as an image
        color = (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200))
        self.pg = pg
        self.screen = screen
        super().__init__(*groups)
        self.image = pg.Surface((30, 10), pg.SRCALPHA)
        pg.draw.polygon(self.image, pg.Color(color), ((0, 0), (50, 15), (0, 30)))
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=(15, 5))

        # Take care of the main stuff
        self.id = id
        self.x = locx  # x position
        self.y = locy  # y position
        self.leaderFlag = leaderflag  # indicates if this agent is a leader or not
        self.orientation = orientation  # what direction the agent is facing (degrees)
        self.speed = speed  # how fast the agent is moving in its given direction (m/s)
        self.leader = leader  # sets this agents leader
        self.sight = sight  # sets how far the agent can see

    def update(self, display=True):  # assumes 1 sec has passed since last move
        rad = (self.orientation / 180) * math.pi  # convert orientation into radians
        self.x = self.x + math.cos(rad) * self.speed  # update x position
        if self.x < 0:
            self.x += 1000
        if self.x > 1000:
            self.x -= 1000

        self.y = self.y + math.sin(rad) * self.speed  # update y position
        if self.y < 0:
            self.y += 1000
        if self.y > 1000:
            self.y -= 1000

        self.rect.center = (self.x, self.y)
        self.image = self.pg.transform.rotate(self.orig_image, (self.orientation * -1))
        self.rect = self.image.get_rect(center=self.rect.center)




