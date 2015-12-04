import pygame
import sys

class PlanetDefense:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((960, 600))
        pygame.display.set_caption("Planet Defense")
        self.exit = False

    def update(self,e):
        pass
    
    def draw(self):
        pass

    def run(self):
        clock = pygame.time.Clock()
        while not self.exit:
            clock.tick(60)
            self.display.fill((0,0,0)) #clear the previous screen
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.exit = True
                print(e)

            self.update(pygame.event) # update the positions etc
            self.draw()               # draw the game screen

            pygame.display.update()

        pygame.quit()
        sys.exit()

game = PlanetDefense()
game.run()