"""
Classes.py that contains different classes and methods
for model.py for the labyrinth's game
Class : Labyrinth, Item, Character
Ludovic GROS
"""

import pygame
import random
from pygame.locals import *
from constant import *


class Labyrinth:

    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generator(self):

        # open the text file with 'r' for reading
        with open(self.file, 'r') as file:
            # list the structure
            structure_lab = []
            for line in file:
                # list each line
                line_lab = []
                for sprite in line:
                    # add the character of each sprite in the list for a line
                    line_lab.append(sprite)
                # add each line in the character list
                structure_lab.append(line_lab)
            # list with each sprite of each lines
            self.structure = structure_lab

    def show(self, window):

        # load the image
        wall_ori = pygame.image.load(WALL_IMG).convert()
        # scale the image with the size of the sprite size
        wall = pygame.transform.scale(wall_ori, (SPT_SZ, SPT_SZ))

        # load the image
        floor_ori = pygame.image.load(FLOOR_IMG).convert()
        # scale the image with the size of the sprite size
        floor = pygame.transform.scale(floor_ori, (SPT_SZ, SPT_SZ))

        # load the image
        floor_f_ori = pygame.image.load(FLOOR_F).convert()
        # scale the image with the size of the sprite size
        floor_f = pygame.transform.scale(floor_f_ori, (SPT_SZ, SPT_SZ))

        # load the image
        guardian_ori = pygame.image.load(GUARDIAN_IMG).convert_alpha()
        # scale the image with a better rendering
        guardian = pygame.transform.smoothscale(guardian_ori, (SPT_SZ, SPT_SZ))

        # position of the starting line number in the structure list
        num_line = 0

        # loop for each line in structure
        for line in self.structure:
            # position of the starting tile in the structure list
            num_tile = 0
            # loop for each sprite in lines
            for sprite in line:
                # X-axis position depending of the sprite position in the list
                x = num_tile * SPT_SZ
                # Y-axis position depending of the line position in the list
                y = num_line * SPT_SZ
                # check the tile if it is a wall
                if sprite == 'w':
                    # paste wall image
                    window.blit(wall, (x, y))
                # check the tile if it is the ending tile
                elif sprite == 'e':
                    # paste the f floor
                    window.blit(floor_f, (x, y))
                # check the tile if it is the guardian position
                elif sprite == 'g':
                    # paste the floor image
                    window.blit(floor, (x, y))
                    # paste the guardian image
                    window.blit(guardian, (x, y))
                # check the tile if it is the dead guardian
                elif sprite == 'd':
                    # paste the floor image instead of the guardian
                    window.blit(floor, (x, y))
                # check the tile if it is the floor
                elif sprite == '0':
                    # paste the floor image
                    window.blit(floor, (x, y))
                # when the loop finish, go to the next sprite
                num_tile += 1
            # when the loop finish, go to the next line
            num_line += 1


class Item:

    def __init__(self, items, lab):

        # load the items image
        item_ori = pygame.image.load(items).convert_alpha()
        # scale the image with the sprite size
        self.items = pygame.transform.smoothscale(item_ori, (SPT_SZ, SPT_SZ))
        self.lab = lab

    def position1(self, window):

        count_max = 1
        count = 0

        # until the maximum objects counter is reach (loop)
        while count < count_max:
            # random number for the x-axis tile position
            self.tile_x = random.randint(0, 14)
            # random number for the y-axis tile position
            self.tile_y = random.randint(0, 14)
            # check if the position is free
            if self.lab.structure[self.tile_y][self.tile_x] == '0':
                # change the list's sprite with the object's tag
                self.lab.structure[self.tile_y][self.tile_x] = 'o1'
                # add one to the object 1 counter
                count += 1
            # if the position is not free
            elif self.lab.structure[self.tile_y][self.tile_x] != '0':
                # nothing happen
                pass

        num_line = 0
        for line in self.lab.structure:
            num_tile = 0
            for sprite in line:
                x = num_tile * SPT_SZ
                y = num_line * SPT_SZ
                # if the sprite is the object's tag
                if sprite == 'o1':
                    # paste item's image
                    window.blit(self.items, (x, y))
                num_tile += 1
            num_line += 1

    def position2(self, window):

        count_max = 1
        count = 0

        while count < count_max:
            self.tile_x = random.randint(0, 14)
            self.tile_y = random.randint(0, 14)
            if self.lab.structure[self.tile_y][self.tile_x] == '0':
                self.lab.structure[self.tile_y][self.tile_x] = 'o2'
                count += 1
            elif self.lab.structure[self.tile_y][self.tile_x] != '0':
                pass

        num_line = 0
        for line in self.lab.structure:
            num_tile = 0
            for sprite in line:
                x = num_tile * SPT_SZ
                y = num_line * SPT_SZ
                if sprite == 'o2':
                    window.blit(self.items, (x, y))
                num_tile += 1
            num_line += 1

    def position3(self, window):

        count_max = 1
        count = 0

        while count < count_max:
            self.tile_x = random.randint(0, 14)
            self.tile_y = random.randint(0, 14)
            if self.lab.structure[self.tile_y][self.tile_x] == '0':
                self.lab.structure[self.tile_y][self.tile_x] = 'o3'
                count += 1
            elif self.lab.structure[self.tile_y][self.tile_x] != '0':
                pass

        num_line = 0
        for line in self.lab.structure:
            num_tile = 0
            for sprite in line:
                x = num_tile * SPT_SZ
                y = num_line * SPT_SZ
                if sprite == 'o3':
                    window.blit(self.items, (x, y))
                num_tile += 1
            num_line += 1


class Character:

    def __init__(self, character, lab):

        # load macgyver's character image
        charac_ori = pygame.image.load(character).convert_alpha()
        # scale macgyver's image with the sprite size
        self.character = pygame.transform.smoothscale(charac_ori, (SPT_SZ, SPT_SZ))
        # x-axis tile position of macgyver
        self.tile_x = 0
        # y-axis tile position of macgyver
        self.tile_y = 7
        # x-axis position of macgyver
        self.x = 0
        # y-axis position of macgyver
        self.y = self.tile_y * SPT_SZ
        self.lab = lab
        # craft counter to craft the f object when all objects are picked up
        self.craft = 0

    def movement(self, character, window):

        floor_ori = pygame.image.load(FLOOR_IMG).convert()
        floor = pygame.transform.scale(floor_ori, (SPT_SZ, SPT_SZ))

        item_ori = pygame.image.load(ITEM_IMG).convert_alpha()
        items1 = pygame.transform.smoothscale(item_ori, (SPT_SZ, SPT_SZ))

        item_ori = pygame.image.load(ITEM2_IMG).convert_alpha()
        items2 = pygame.transform.smoothscale(item_ori, (SPT_SZ, SPT_SZ))

        item_ori = pygame.image.load(ITEM3_IMG).convert_alpha()
        items3 = pygame.transform.smoothscale(item_ori, (SPT_SZ, SPT_SZ))

        item_ori = pygame.image.load(ITEM4_IMG).convert_alpha()
        items4 = pygame.transform.smoothscale(item_ori, (SPT_SZ, SPT_SZ))

        inventory_ori = pygame.image.load(INVENTORY).convert_alpha()
        inventory = pygame.transform.scale(inventory_ori, (SPT_SZ, SPT_SZ))

        # if the player press the right arrow
        if character == 'right':
            # check if x-axis where is macgyver, is < to max sprite nnb
            if self.tile_x < (SPT_NB_SD - 1):
                # check if the position at the right of mcgyver is not a wall
                if self.lab.structure[self.tile_y][self.tile_x+1] != 'w':
                    # moves macgyver to the right
                    self.tile_x += 1
                    self.x = self.tile_x * SPT_SZ
                    # check if the resultant position is an object
                    if self.lab.structure[self.tile_y][self.tile_x] == 'o1':
                        # tag the sprite with the object
                        self.lab.structure[self.tile_y][self.tile_x] = 'i1'
                        # add 1 to the craft counter
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'o2':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i2'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'o3':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i3'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'g' and self.craft == 3:
                        self.lab.structure[self.tile_y][self.tile_x] = 'd'

        # if the player press the left arrow
        if character == 'left':
            # check if the x-axis tile where is mcgyver, is > to min sprite nb
            if self.tile_x > 0:
                # check if the position at the left of macgyver is not a wall
                if self.lab.structure[self.tile_y][self.tile_x-1] != 'w':
                    self.tile_x -= 1
                    self.x = self.tile_x * SPT_SZ
                    if self.lab.structure[self.tile_y][self.tile_x] == 'o1':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i1'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'o2':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i2'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'o3':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i3'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'g' and self.craft == 3:
                        self.lab.structure[self.tile_y][self.tile_x] = 'd'

        # if the player press the up arrow
        if character == 'up':
            # check if y-axis where is mcgyver, is > to the min sprite nb
            if self.tile_y > 0:
                # check if the position above macgyver is not a wall
                if self.lab.structure[self.tile_y-1][self.tile_x] != 'w':
                    self.tile_y -= 1
                    self.y = self.tile_y * SPT_SZ
                    if self.lab.structure[self.tile_y][self.tile_x] == 'o1':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i1'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'o2':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i2'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'o3':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i3'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'g' and self.craft == 3:
                        self.lab.structure[self.tile_y][self.tile_x] = 'd'

        # if the player press the up arrow
        if character == 'down':
            # check if y-axis tile where is macgyver, is < to the max sprite nb
            if self.tile_y < (SPT_NB_SD - 1):
                # check if the position below macgyver is not a wall
                if self.lab.structure[self.tile_y+1][self.tile_x] != 'w':
                    self.tile_y += 1
                    self.y = self.tile_y * SPT_SZ
                    if self.lab.structure[self.tile_y][self.tile_x] == 'o1':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i1'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'o2':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i2'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'o3':
                        self.lab.structure[self.tile_y][self.tile_x] = 'i3'
                        self.craft += 1
                    elif self.lab.structure[self.tile_y][self.tile_x] == 'g' and self.craft == 3:
                        self.lab.structure[self.tile_y][self.tile_x] = 'd'

        num_line = 0
        for line in self.lab.structure:
            num_tile = 0
            for sprite in line:
                x = num_tile * SPT_SZ
                y = num_line * SPT_SZ
                if sprite == 'i1':
                    # show the item picked up in the inventory
                    window.blit(items1, (0, SPT_NB_SD * SPT_SZ))
                    # replace the item picked up in the lab with the floor
                    window.blit(floor, (x, y))
                elif sprite == 'i2':
                    window.blit(items2, (1 * SPT_SZ, SPT_NB_SD * SPT_SZ))
                    window.blit(floor, (x, y))
                elif sprite == 'i3':
                    window.blit(items3, (2 * SPT_SZ, SPT_NB_SD * SPT_SZ))
                    window.blit(floor, (x, y))
                # if the craft number reach 3, craft the 4th item
                elif self.craft == 3:
                    # show the item in the inventory bar below the labyrinth
                    window.blit(items4, (3 * SPT_SZ, SPT_NB_SD * SPT_SZ))
                    # replace the image of items to remove its
                    window.blit(inventory, (0, SPT_NB_SD * SPT_SZ))
                    window.blit(inventory, (1 * SPT_SZ, SPT_NB_SD * SPT_SZ))
                    window.blit(inventory, (2 * SPT_SZ, SPT_NB_SD * SPT_SZ))
                elif sprite == 'd':
                    window.blit(floor, (x, y))
                num_tile += 1
            num_line += 1
