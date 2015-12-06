import pygame
from math import atan2, sqrt, cos, sin


class Ship(object):
    """
    A class that represents a ship.
    This class has to be inherited from.
    """

    max_hp = 10
    damage = 1
    range = 50
    atk = 1
    _spritePath = ''
    orbiting_speed = .005

    def __init__(self, start_pos=(150, 150), max_hp=max_hp, atk=atk, orbiting=False, screen_size=()):
        self.hp = max_hp
        self.screen_size = screen_size
        self.orbiting = orbiting
        self.atk = atk
        self.x = start_pos[0]
        self.y = start_pos[1]
        self._spritePath = "assets/sprites/ship.png"
        self.sprite = pygame.image.load(self._spritePath).convert()

    def update(self):
        if self.orbiting:
            # coords considering the origin to be the center
            x, y = self.x - self.screen_size[0] / 2, self.y - self.screen_size[1] / 2

            # getting the angle and radius
            angle = atan2(y, x)
            radius = sqrt(x ** 2 + y ** 2)

            # orbit a little bit
            angle += self.orbiting_speed

            x, y = radius * cos(angle), radius * sin(angle)

            # back to top-left origin
            self.x, self.y = x + self.screen_size[0] / 2, y + self.screen_size[1] / 2
