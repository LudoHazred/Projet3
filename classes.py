"""
Classes.py that contains different classes and methods for model.py for the labyrinth.
Class : Labyrinth
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
    	#open the text file with 'r' for reading
        with open(self.file, 'r') as file:
        	#liste de chaque ligne
            structure_lab = []
            for line in file:
            	#liste de chaque sprite dans chaque ligne
                line_lab = []
                for sprite in line:
                    line_lab.append(sprite)
                structure_lab.append(line_lab)
            self.structure = structure_lab

    def show(self, window):
        wall_original = pygame.image.load(WALL_IMAGE).convert()
        wall = pygame.transform.scale(wall_original, (SPRITE_SIZE, SPRITE_SIZE))

        floor_original = pygame.image.load(FLOOR_IMAGE).convert()
        floor = pygame.transform.scale(floor_original, (SPRITE_SIZE, SPRITE_SIZE))

        floor_final_original = pygame.image.load(FLOOR_FINAL_TILE).convert()
        floor_final = pygame.transform.scale(floor_final_original, (SPRITE_SIZE, SPRITE_SIZE))

        guardian_original = pygame.image.load(GUARDIAN_IMAGE).convert_alpha()
        guardian = pygame.transform.smoothscale(guardian_original, (SPRITE_SIZE, SPRITE_SIZE))

        item_original = pygame.image.load(ITEM_IMAGE).convert_alpha()
        items = pygame.transform.smoothscale(item_original, (SPRITE_SIZE, SPRITE_SIZE))

        num_line = 0
        for line in self.structure:
            num_tile = 0
            for sprite in line:
                x = num_tile * SPRITE_SIZE
                y = num_line * SPRITE_SIZE
                if sprite == 'w':
                    window.blit(wall, (x, y))
                elif sprite == 'e':
                    window.blit(floor_final, (x, y))
                elif sprite == 'g':
                    window.blit(floor, (x, y))
                    window.blit(guardian, (x, y))
                elif sprite == '0':
                    window.blit(floor, (x, y))
                elif sprite == 'o':
                    window.blit(floor, (x, y))
                    window.blit(items, (x, y))
                #when the loop finish to paste the image, go to the next sprite
                num_tile += 1
            #when the loop finish, go to the next line
            num_line += 1


class Item:

    def __init__(self, items, lab):
        item_original = pygame.image.load(ITEM_IMAGE).convert_alpha()
        self.items = pygame.transform.smoothscale(item_original, (SPRITE_SIZE, SPRITE_SIZE))
        #self.x = random.randint(1, 15) * SPRITE_SIZE
        #self.y = random.randint(1, 15) * SPRITE_SIZE
        self.lab = lab


class Character:

    def __init__(self, character, lab):

        charac_ori = pygame.image.load(character).convert_alpha()
        self.character = pygame.transform.smoothscale(charac_ori, (SPRITE_SIZE, SPRITE_SIZE))
        self.tile_x = 0
        self.tile_y = 7
        self.x = 0
        self.y = self.tile_y * SPRITE_SIZE
        self.lab = lab

    def movement(self, character):

        if character == 'right':
            if self.tile_x < (SPRITE_NUMBER_SIDE - 1):
                if self.lab.structure[self.tile_y][self.tile_x+1] != 'w':
                    self.tile_x += 1
                    self.x = self.tile_x * SPRITE_SIZE

        if character == 'left':
            if self.tile_x > 0:
                if self.lab.structure[self.tile_y][self.tile_x-1] != 'w':
                    self.tile_x -= 1
                    self.x = self.tile_x * SPRITE_SIZE

        if     character == 'up':
            if self.tile_y > 0:
                if self.lab.structure[self.tile_y-1][self.tile_x] != 'w':
                    self.tile_y -= 1
                    self.y = self.tile_y * SPRITE_SIZE

        if character == 'down':
            if self.tile_y < (SPRITE_NUMBER_SIDE - 1):
                if self.lab.structure[self.tile_y+1][self.tile_x] != 'w':
                    self.tile_y += 1
                    self.y = self.tile_y * SPRITE_SIZE
