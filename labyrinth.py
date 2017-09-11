"""
Labyrinth game where Macgyver needs to collect objects to neutralize the guardian
to escpe the LAByrinth.
File : labyrinth.py, classes.py, constant.py
"""

import pygame
from pygame.locals import *
from constant import *
from classes import *

#module initialization
pygame.init()

#display the window's game
window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))

#LAByrinth generation
LAB = Labyrinth('structure.txt')
LAB.generator()
LAB.show(window)

#MACGYVER generation
MACGYVER = Character("images/MACGYVER.png", LAB)

#ITEM generation
ITEM = Item("images/object.png", LAB)

#paste image in the window's game
window.blit(MACGYVER.character, (MACGYVER.x, MACGYVER.y))

#refresh the display
pygame.display.flip()

LOOP = 1
while LOOP:

    pygame.time.Clock().tick(30)


    for event in pygame.event.get():
        if event.type == QUIT:
            LOOP = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                LOOP = 0
            elif event.key == K_RIGHT:
                MACGYVER.movement('right')
            elif event.key == K_LEFT:
                MACGYVER.movement('left')
            elif event.key == K_UP:
                MACGYVER.movement('up')
            elif event.key == K_DOWN:
                MACGYVER.movement('down')

    LAB.show(window)
    window.blit(MACGYVER.character, (MACGYVER.x, MACGYVER.y))
    pygame.display.flip() #rafraichissement de l'écran

    if LAB.structure[MACGYVER.tile_y][MACGYVER.tile_x] == 'o':
        window.blit(ITEM.items, (0, 0))
        window.blit(MACGYVER.character, (MACGYVER.x, MACGYVER.y))
        pygame.display.flip() #rafraichissement de l'écran

    if LAB.structure[MACGYVER.tile_y][MACGYVER.tile_x] == 'g':
        pass

    if LAB.structure[MACGYVER.tile_y][MACGYVER.tile_x] == 'e':
        LOOP = 0
