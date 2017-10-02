"""
Labyrinth game where Macgyver needs to collect objects to neutralize the guardian
to escpe the labyrinth.
File : labyrinth.py, classes.py, constant.py
"""

import pygame
from pygame.locals import *
from constant import *
from classes import *

# variable booléenne au début true, relance false et si mort test valeur de relance si true (voir en menu)
# menu avec choix de quitter le jeu, relancer la partie si mort, et touche associé pour enclencher le menu

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
item1 = Item(ITEM_IMAGE, lab)
item2 = Item(ITEM2_IMAGE, lab)
item3 = Item(ITEM3_IMAGE, lab)
# loop relance
item1.position1(window)
item2.position2(window)
item3.position3(window)

# paste image in the window's game
window.blit(macgyver.character, (macgyver.x, macgyver.y))

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

    lab.show(window)
    window.blit(macgyver.character, (macgyver.x, macgyver.y))
    # rafraichissement de l'écran
    pygame.display.flip()

    if lab.structure[macgyver.tile_y][macgyver.tile_x] == 'g' and macgyver.craft != 3:
        print('Game Over')
        # remplacer par menu
        loop = False

    if lab.structure[macgyver.tile_y][macgyver.tile_x] == 'e':
        print('You are free')
        # remplacer par écran de victoire
        loop = False
