import pygame

class Player(object):
    '''
    A class that is supposed to represent the player
    '''

    _spritePath = ''

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Player')
        self.max_hearts = kwargs.get('max_hearts', 3)
        self.hearts = kwargs.get('hearts', self.max_hearts)
        self._spritePath = kwargs.get('sprite', 'assets/sprites/earth.png')
        self.sprite = pygame.image.load(self._spritePath).convert()
        
        self.posX = 480
        self.posY = 300
        self.score = 0
        self.kills = 0

        self.ships = []