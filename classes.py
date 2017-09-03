import pygame
from pygame.locals import *
from constant import *

class Labyrinth:
	def __init__(self, file):
		self.file = file
		self.structure = 0

	def generator(self):
		with open(self.file, 'r') as file: #'r' pour read only 'w' pour only writing 'a' pour appending
			structure_lab = [] #liste de chaque ligne
			for line in file:
				line_lab =[] #liste de chaque sprite dans chaque ligne
				for sprite in line:
					line_lab.append(sprite)
				structure_lab.append(line_lab)
			self.structure = structure_lab

	def show(self, window):
		wall_original = pygame.image.load(wall_image).convert()
		wall = pygame.transform.scale(wall_original, (sprite_size, sprite_size))

		floor_original = pygame.image.load(floor_image).convert()
		floor = pygame.transform.scale(floor_original, (sprite_size,sprite_size))

		floor_final_original = pygame.image.load(floor_final_tile).convert()
		floor_final = pygame.transform.scale(floor_final_original, (sprite_size,sprite_size))

		guardian_original = pygame.image.load(guardian_image).convert_alpha()
		guardian = pygame.transform.smoothscale(guardian_original, (sprite_size,sprite_size))

		num_line = 0
		for line in self.structure:
			num_tile = 0
			for sprite in line:
				x = num_tile * sprite_size
				y = num_line * sprite_size
				if sprite == 'w':
					window.blit(wall, (x,y))
				elif sprite == 'a':
					window.blit(floor_final, (x,y))
				elif sprite == 'g':
					window.blit(floor, (x,y))
					window.blit(guardian, (x,y))
				elif sprite == '0':
					window.blit(floor, (x,y))
				num_tile +=1 #quand la boucle fini de coller l'image sur le premier sprite passe au suivant toujours dans la même ligne
			num_line +=1 #quand la boucle fini de coller une ligne pas à la suivante

class Character:

	def __init__(self, character, lab):

		character_original = pygame.image.load(character).convert_alpha()
		self.character = pygame.transform.smoothscale(character_original, (sprite_size,sprite_size))
		self.tile_x = 0
		self.tile_y = 7
		self.x = 0
		self.y = self.tile_y * sprite_size
		self.lab = lab

	def movement(self, character):

		if character == 'right':
			if self.tile_x < (sprite_number_side - 1):
				if self.lab.structure[self.tile_y][self.tile_x+1] != 'w':
					self.tile_x += 1
					self.x = self.tile_x * sprite_size

		if character == 'left':
			if self.tile_x > 0:
				if self.lab.structure[self.tile_y][self.tile_x-1] != 'w':
					self.tile_x -= 1
					self.x = self.tile_x * sprite_size

		if 	character == 'up':
			if self.tile_y > 0:
				if self.lab.structure[self.tile_y-1][self.tile_x] != 'w':
					self.tile_y -= 1
					self.y = self.tile_y * sprite_size

		if character == 'down':
			if self.tile_y < (sprite_number_side - 1):
				if self.lab.structure[self.tile_y+1][self.tile_x] != 'w':
					self.tile_y += 1
					self.y = self.tile_y * sprite_size