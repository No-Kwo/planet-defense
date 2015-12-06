from math import sqrt, cos, sin, radians

import pygame
import random


class Enemy(object):
    """
    A class that represents an ennemy.
    This class has to be inherited from.
    """

    max_hp = 10
    speed = 1.0
    damage = 1
    _spritePath = ''

    def __init__(self, screen_size, max_hp=max_hp):
        self.speed = random.uniform(0.75, 1.75)
        self.screen_size = screen_size
        self.max_hp = max_hp
        rand = random.randint(1, 6)  # very basic way to decide which asteriod to spawn
        self.damage = rand
        self._spritePath = "assets/sprites/a{0}".format(rand) + ".png"
        self.sprite = pygame.image.load(self._spritePath).convert_alpha()

        # random spawn
        self.radius = sqrt(self.screen_size[0] ** 2 + self.screen_size[1] ** 2) / 2.
        print cos(radians(180))
        # random angle
        self.angle = random.randint(0, 360)
        print(self.angle)
        self.x = self.radius * cos(self.angle) + self.screen_size[0] / 2.
        self.y = self.radius * sin(self.angle) + self.screen_size[1] / 2.
        # print(self.x, self.y)

    def update(self):
        self.radius -= self.speed
        self.y = self.radius * sin(self.angle) + self.screen_size[1] / 2.
        self.x = self.radius * cos(self.angle) + self.screen_size[0] / 2.
