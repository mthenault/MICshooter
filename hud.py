import os
import common_pygame
import random
pygame = common_pygame.pygame
screen= common_pygame.screen

class Hud():
	def __init__(self, single_sprites):
		self.single_sprites=single_sprites
			# Create a font
		self.tinyfont = pygame.font.Font(None, 16)
		self.font = pygame.font.Font(None,32)
		self.font2 = pygame.font.Font(None, 150)
		self.score_label = self.tinyfont.render("score", True, (255,255, 0))
		self.inf = self.font.render("Inf.", True, (0,130, 255))
		
	def blit(self, ship, level):
			# Render the text
		life_txt = self.font.render(str(ship.life), True, (255,0, 0))
		score_txt = self.font.render(str(ship.score), True, (255,255, 255))
		armor_txt = self.font.render(str(ship.armor), True, (255,255, 0))
		level_txt = self.tinyfont.render("level " + str(level), True, (255,255, 0))
		#show the HUD
		screen.blit(self.single_sprites['lifemask.png'],(0,
		600-self.single_sprites['lifemask.png'].get_height() ))
		#show the life and the score
		screen.blit(life_txt, (common_pygame.screenwidth-70,common_pygame.screenheight-224 ))
		screen.blit(self.score_label, (350-35,common_pygame.screenheight-215 ))
		screen.blit(score_txt, (350,common_pygame.screenheight-224 ))
		screen.blit(level_txt, (455,common_pygame.screenheight-215 ))
		screen.blit(armor_txt, (35,common_pygame.screenheight-227 ))
		
		#blit the current weapon and the ammo
		if ship.weapon==1:
			
			screen.blit(self.single_sprites['sprite_laser.png'],(160, common_pygame.screenheight-220 ))
			screen.blit(self.inf,(185, common_pygame.screenheight-227 ))
		else:
			ammo_txt = self.font.render(str(ship.ammo), True, (0,130, 255))
			screen.blit(self.single_sprites['ball1.png'],(160, common_pygame.screenheight-220 ))
			screen.blit(ammo_txt,(185, common_pygame.screenheight-227 ))
