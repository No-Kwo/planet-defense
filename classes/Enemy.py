import pygame
import random

class Enemy(object):
    '''
    A class that represents an ennemy.
    This class has to be inherited from.
    '''

    max_hp = 10
    speed = 1.0
    damage = 1
    _spritePath = ''
    posX = 50
    posY = 50

    def __init__(self, screen_size, max_hp=max_hp):
        self.max_hp = max_hp
        rand = random.randint(1,6); #very basic way to decide which asteriod to spawn
        self.damage = rand
        self._spritePath = "assets/sprites/a{0}".format(rand)+".png"
        self.sprite = pygame.image.load(self._spritePath).convert()

        # random spawn
        r = random.randint(0,3) # 0 - left , 1 right 2 top 3 bottom
        if r==0:
            self.posX = 0
            self.posY = random.randint(0,screen_size[1])
        elif r==1:
            self.posX = screen_size[0]
            self.posY = random.randint(0,screen_size[1])
        elif r==2:
            self.posX = random.randint(0,screen_size[0])
            self.posY = 0
        elif r==3:
            self.posX = random.randint(0,screen_size[0])
            self.posY = screen_size[1]


    def update(self,target): #move towards the target
        speed = self.speed
        if(self.posX>target[0]):
            self.posX-=speed;
        else:
            self.posX+=speed;

        if(self.posY>target[1]):
            self.posY-=speed;
        else:
            self.posY+=speed;