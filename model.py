"""
McGyver Labyrinth Game
You must find all objects to beat the guardian and escape from the labyrinth

Python Script
Files : model.py, classes.py, constantes.py, n1 + images
"""

#Importation of necessary library
import pygame
from pygame.locals import *

from classes import *
from constant import *

#initialisation of the library
pygame.init()

#Creation of the window
window = pygame.display.set_mode((window_side, window_side))

#Title
pygame.display.set_caption(title_window)

#

#Screen refresh
pygame.display.flip()

#Principal loop (menu loop and end loop)
loop = 1
while loop:
	pygame.time.Clock().tick(30) #loop limitation speed (30 frames per s)
	for event in pygame.event.get():
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			loop = 0