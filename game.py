import pygame

pygame.init()
display = pygame.display.set_mode(800, 500)

clock = pygame.time.Clock()

shut = False
while not shut:

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			shut = True

		print(e)

	pygame.display.update()
	clock.tick(60)

pygame.quit()