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
					#if sprite != '/n': #ne prend pas en compte le retour à la ligne
						line_lab.append(sprite)
				structure_lab.append(line_lab)
			self.structure = structure_lab

	def show(self, window):
		wall = pygame.image.load(wall_image).convert()
		floor = pygame.image.load(floor_image).convert()
		floor_final = pygame.image.load(floor_final_tile).convert()
		guardian = pygame.image.load(guardian_image).convert_alpha()

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
					window.blit(guardian, (x,y))
				elif sprite == '0':
					window.blit(floor, (x,y))
				num_tile +=1 #quand la boucle fini de coller l'image sur le premier sprite passe au suivant toujours dans la même ligne
			num_line +=1 #quand la boucle fini de coller une ligne pas à la suivante

