"""
Labyrinth's game where Macgyver needs to collect 3 objects
to neutralize the guardian and to escape the labyrinth.
File : labyrinth.py, classes.py, constant.py, structure.txt
Ludovic GROS
"""

import os
import pygame
from pygame.locals import *
from constant import *
from classes import *

# module initialization
pygame.init()

# display the window's game
window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE + SPT_SZ))

# main loop that allows multiple loop for menu and game (win/loose)
loop = True
while loop:

    # loop limitation speed
    pygame.time.Clock().tick(30)

    main_menu = True
    loop_end = True
    loop_win = True
    bad_end = 0
    good_end = 0

    while main_menu:

        # loop limitation speed
        pygame.time.Clock().tick(30)

        # Load and display the menu
        homepage = pygame.image.load(HOMEPAGE).convert()
        window.blit(homepage, (0, 0))

        # refresh the display
        pygame.display.flip()

        loop_menu = True
        loop_game = True

        while loop_menu:

            # loop limitation speed
            pygame.time.Clock().tick(30)

            # loop to check when the player makes an action
            for event in pygame.event.get():

                # if the player try to quit
                if event.type == QUIT:
                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop = False

                # to quit when the player press escape
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop = False

                # if the player press a key
                elif event.type == KEYDOWN:

                    # start the game when the player press F1
                    if event.key == K_F1:
                        loop_menu = False
                        menu = 1

        # check if the player pressed F1
        if menu != 0:

            # hide the menu by a black background
            background = pygame.image.load(BACKGROUND).convert()
            window.blit(background, (0, 0))

            # labyrinth generation
            lab = Labyrinth('structure.txt')
            lab.generator()

            # display the labyrinth on the background
            lab.show(window)

            # macgyver generation
            macgyver = Character("images/macgyver.png", lab)

            # item generation
            item1 = Item(ITEM_IMG, lab)
            item2 = Item(ITEM2_IMG, lab)
            item3 = Item(ITEM3_IMG, lab)

            # display items in the labyrinth
            item1.position1(window)
            item2.position2(window)
            item3.position3(window)

        # game's loop
        while loop_game:

            # display the labyrinth in the game's loop
            lab.show(window)

            # display macgyver in the labyrinth
            window.blit(macgyver.character, (macgyver.x, macgyver.y))

            # loop limitation speed
            pygame.time.Clock().tick(30)

            # refresh the display
            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:

                    # if the player try to quit, return to menu
                    loop_game = False
                    loop = False

                elif event.type == KEYDOWN:

                    if event.key == K_ESCAPE:

                        # if the player press escape, return to menu
                        loop_game = False

                    elif event.key == K_RIGHT:

                        # if the player press right arrow, moves macgyver right
                        macgyver.movement('right', window)

                    elif event.key == K_LEFT:

                        # if the player press left arrow, moves mcgyver left
                        macgyver.movement('left', window)

                    elif event.key == K_UP:

                        # if the player press up arrow, moves mcgyver up
                        macgyver.movement('up', window)

                    elif event.key == K_DOWN:

                        # if the player press down arrow, moves mcgyver down
                        macgyver.movement('down', window)

                    # display the labyrinth after player's action
                    lab.show(window)

                    # display macgyver in the labyrinth after player's ation
                    window.blit(macgyver.character, (macgyver.x, macgyver.y))

                    # refresh the display after player's action
                    pygame.display.flip()

            # check conditions if the player looses
            if lab.structure[macgyver.tile_y][macgyver.tile_x] == 'g' and macgyver.craft != 3:
                loop_game = False
                loop_menu = False
                main_menu = False
                bad_end = 1

            # check conditions if the player wins
            if lab.structure[macgyver.tile_y][macgyver.tile_x] == 'e':
                loop_game = False
                loop_menu = False
                main_menu = False
                good_end = 1

    # looser's loop
    while loop_end:

        # check if the player lost the game
        if bad_end != 0:

            # close the game
            main_menu = False
            loop_menu = False
            loop_game = False

            # load and display the bad ending menu
            loose = pygame.image.load(LOOSE).convert()
            window.blit(loose, (0, 0))

            # refresh the display after the player lost
            pygame.display.flip()

            # loop limitation speed
            pygame.time.Clock().tick(30)

            # check player's action in the loose menu
            for event in pygame.event.get():

                # when player press F1
                if event.type == KEYDOWN and event.key == K_F1:

                    # return to main menu
                    loop_end = False

                # quit the game
                if event.type == QUIT:

                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop_end = False
                    loop_win = False
                    loop = False

                # to quit when the player press escape
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop_end = False
                    loop_win = False
                    loop = False

        # no ending menu if the player didn't loose
        elif bad_end == 0:
            loop_end = False

    # winner's loop
    while loop_win:

        # check if the player wins
        if good_end != 0:

            # close the game
            main_menu = False
            loop_menu = False
            loop_game = False

            # load and display the winning menu
            win = pygame.image.load(WIN).convert()
            window.blit(win, (0, 0))

            # refresh the display after the player wins
            pygame.display.flip()

            # loop limitation speed
            pygame.time.Clock().tick(30)

            # check player's action in the loose menu
            for event in pygame.event.get():

                # when player press F1
                if event.type == KEYDOWN and event.key == K_F1:

                    # return to main menu
                    loop_win = False

                # when press escape or quit, quit the game
                if event.type == QUIT:
                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop_win = False
                    loop = False

                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    loop_menu = False
                    loop_game = False
                    main_menu = False
                    loop_win = False
                    loop = False

        # no ending menu if the player didn't win
        elif good_end == 0:
            loop_win = False
