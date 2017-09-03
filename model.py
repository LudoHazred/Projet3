import pygame
from pygame.locals import *

from constant import *
from classes import *

#initialisation des modules
pygame.init()

window = pygame.display.set_mode((window_side, window_side))


lab = Labyrinth('structure.txt')
lab.generator()
lab.show(window)

macgyver = Character("images/macgyver.png", lab)

window.blit(macgyver.character, (macgyver.x, macgyver.y))

pygame.display.flip()

loop = 1
while loop:

	pygame.time.Clock().tick(30)


	for event in pygame.event.get():
		if event.type == QUIT:
			loop = 0
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				loop = 0
			elif event.key == K_RIGHT:
				macgyver.movement('right')
			elif event.key == K_LEFT:
				macgyver.movement('left')
			elif event.key == K_UP:
				macgyver.movement('up')
			elif event.key == K_DOWN:
				macgyver.movement('down')

	lab.show(window)
	window.blit(macgyver.character, (macgyver.x, macgyver.y))
	pygame.display.flip() #rafraichissement de l'écran