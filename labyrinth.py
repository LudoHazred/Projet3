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

loop = True
while loop:
    main_menu = True
    loop_end = True
    loop_win = True
    bad_end = 0
    good_end = 0

    while main_menu:
        # Load and display the menu
        homepage = pygame.image.load(HOMEPAGE).convert()
        window.blit(homepage, (0,0))

        # refresh the display
        pygame.display.flip()
    
        loop_menu = True
        loop_game = True

        while loop_menu:

    	    # loop limitation speed
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop = False

                elif event.type == KEYDOWN:
            	    # start the game
            	    if event.key == K_F1:
            		    loop_menu = False
            		    menu = 1

        if menu != 0:

            background = pygame.image.load(BACKGROUND).convert()
            window.blit(background, (0,0))

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

        # game's loop
        while loop_game:

            lab.show(window)
            window.blit(macgyver.character, (macgyver.x, macgyver.y))
            pygame.time.Clock().tick(30)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    loop_game = False
                    loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        loop_game = False
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
                loop_game = False
                loop_menu = False
                main_menu = False
                bad_end = 1

            if lab.structure[macgyver.tile_y][macgyver.tile_x] == 'e':
                loop_game = False
                loop_menu = False
                main_menu = False
                good_end = 1

    while loop_end:
        if bad_end != 0:
            main_menu = False
            loop_menu = False
            loop_game = False
            loose = pygame.image.load(LOOSE).convert()
            window.blit(loose, (0,0))
            pygame.display.flip()
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_F1:
                    loop_end = False
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop_end = False
                    loop_win = False
                    loop = False
        elif bad_end == 0:
            loop_end = False

    while loop_win:
        if good_end != 0:
            main_menu = False
            loop_menu = False
            loop_game = False
            win = pygame.image.load(WIN).convert()
            window.blit(win, (0,0))
            pygame.display.flip()
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_F1:
                    loop_end = False
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop_win = False
                    loop = False
        elif good_end == 0:
            loop_win = False