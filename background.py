import os
import common_pygame
import random
pygame = common_pygame.pygame
screen= common_pygame.screen

class BackGen():
	
	
	def __init__(self, single_sprites):
		self.single_sprites=single_sprites
		self.compteur=0
		self.asteroidList=list()
		self.ast = self.single_sprites['asteroid1.png']
		self.rotateAst=0
		
	def updatecompteur(self):
		self.compteur=self.compteur+1
		
	def blitStars(self):
		screen.blit(self.single_sprites['background.png'],(0,-600+(self.compteur%200*3)))
		screen.blit(self.single_sprites['background.png'],(0,self.compteur%200*3))
		
	def determine(self, x):
		(x_, y, v, s, sprite, h, w) = x
		if y-h>=screen.get_height():
			return True
		return False
		
	def blitPlanets(self):
		if len(self.asteroidList)<=2 and self.compteur%10==0:
			#x, y, speed, size, sprite, height
			size = random.randrange(10, 200)
			
			
			asteroid=False
			#load the appropriate sprite
			choix = random.randrange(1,4)
			if choix==1:
				spritearg = pygame.transform.scale(self.single_sprites['planet1.png'], (size , size )).convert_alpha()
			elif choix==2:
				spritearg = pygame.transform.scale(self.single_sprites['planet2.png'], (size , size )).convert_alpha()
			else:
				spritearg = pygame.transform.scale(self.single_sprites['planet3.png'], (size , size )).convert_alpha()

			speed = random.randrange(2, 4)
			
			height = spritearg.get_height()
			width = spritearg.get_width()
			self.asteroidList.append((random.randrange(0, screen.get_width()),0, speed, size ,spritearg, height, width))
			
		#determine : false if keep, true if delete
		self.asteroidList[:] = [x for x in self.asteroidList if not self.determine(x)]
		
		for index in xrange(len(self.asteroidList)):
			(x, y, v, s, sprite, h, w) = self.asteroidList[index]	
			screen.blit(sprite,(x, y-h))
			y=y+v
			self.asteroidList[index]=(x, y, v, s, sprite, h, w)
				
		
	def blitFog(self):
		screen.blit(self.single_sprites['backgroundtransp.png'],(0,-600+(self.compteur%40*15)))
		screen.blit(self.single_sprites['backgroundtransp.png'],(0,self.compteur%40*15))
	

