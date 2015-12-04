import pygame
from classes.player import Player
from classes.ship import Ship
from classes.enemy import Enemy
import sys
import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

class PlanetDefense:

    mousePos = (100,100) #current mouse position
    screenSize = (960,600)
    ships = []
    enemies = []

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Planet Defense")
        self.display = pygame.display.set_mode(self.screenSize)
        
        self.exit = False
        self.players = [Player()]

    def update(self,e):
        for s in self.enemies:
            s.update(self.screenSize)
    #    for object in self.enemies,self.ships,self.players:
         #   object.update()
    
    def draw_sprite(self,sprite,position):
        self.display.blit(sprite,(position[0]-sprite.get_size()[0]/2,position[1]-sprite.get_size()[1]/2))

    def draw(self):
        self.draw_sprite(self.players[0].sprite,(self.screenSize[0]/2,self.screenSize[1]/2))

        for s in self.ships+self.enemies:
            self.draw_sprite(s.sprite,(s.posX,s.posY))

    def build_ship(self):
        print(pygame.mouse.get_pos())
        self.ships.append(Ship(pygame.mouse.get_pos()))

    def spawn_asteroid(self):
        self.enemies.append(Enemy((self.screenSize[0]/2,self.screenSize[1]/2)))

    def run(self):
        clock = pygame.time.Clock()
        set_interval(self.spawn_asteroid,1)
        while not self.exit:
            clock.tick(60)
            self.display.fill((0,0,0)) #clear the previous screen
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.exit = True
                elif e.type == pygame.MOUSEMOTION:
                    self.mousePos = e.pos
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    self.build_ship()
                print(e)
            self.update(pygame.event) # update the positions etc
            self.draw()               # draw the game screen

            pygame.display.update()

        pygame.quit()
        sys.exit()

game = PlanetDefense()
game.run()