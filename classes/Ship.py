import pygame

class Ship(object):
    '''
    A class that represents a ship.
    This class has to be inherited from.
    '''

    max_hp = 10
    damage = 1
    range = 50
    atk = 1
    _spritePath = ''

    def __init__(self, start_pos=(150,150), max_hp=max_hp, atk=atk, orbiting=False):
        self.hp = max_hp
        self.orbiting = orbiting
        self.atk = atk
        self.posX = start_pos[0]
        self.posY = start_pos[1]
        self._spritePath = "assets/sprites/ship.png"
        self.sprite = pygame.image.load(self._spritePath).convert()