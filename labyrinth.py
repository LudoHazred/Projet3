"""
Labyrinth game where Macgyver needs to collect objects to neutralize the guardian
to escpe the labyrinth.
File : labyrinth.py, classes.py, constant.py
"""

import pygame
from pygame.locals import *
from constant import *
from classes import *

# module initialization
pygame.init()

# display the window's game
window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE + SPRITE_SIZE))

# labyrinth generation
lab = Labyrinth('structure.txt')
lab.generator()
lab.show(window)

# macgyver generation
macgyver = Character("images/macgyver.png", lab)


# item generation
item = Item("images/object.png", lab)
item.position(window)

# paste image in the window's game
window.blit(macgyver.character, (macgyver.x, macgyver.y))

window.blit(item.items, (item.x_item, item.y_item))

# refresh the display
pygame.display.flip()

loop = True
while loop:

    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                loop = False
            elif event.key == K_RIGHT:
                macgyver.movement('right', window)
            elif event.key == K_LEFT:
                macgyver.movement('left', window)
            elif event.key == K_UP:
                macgyver.movement('up', window)
            elif event.key == K_DOWN:
                macgyver.movement('down', window)

    window.blit(item.items, (item.x_item, item.y_item))
    lab.show(window)
    window.blit(macgyver.character, (macgyver.x, macgyver.y))
    # rafraichissement de l'écran
    pygame.display.flip()        

    if lab.structure[macgyver.tile_y][macgyver.tile_x] == 'e':
        loop = False
