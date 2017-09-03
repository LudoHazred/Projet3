import pygame
from pygame.locals import *

from constant import *
from classes import *

#initialisation des modules
pygame.init()

window = pygame.display.set_mode((window_side, window_side))

loop = 1
while loop:
	lab = Labyrinth('structure.txt')
	lab.generator()
	lab.show(window)
	pygame.time.Clock().tick(30)
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == QUIT:
			loop = 0
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				loop = 0
			elif event.key == K_RIGHT:
				macgyver.move()
			elif event.key == K_LEFT:
				macgyver.move()
			elif event.key == K_UP:
				macgyver.move()
			elif event.key == K_DOWN:
				macgyver.move()

	lab.show(window)
	pygame.display.flip() #rafraichissement de l'écran