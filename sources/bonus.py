import os
import common_pygame
import random
pygame = common_pygame.pygame
screen= common_pygame.screen

class Bonus():
	def __init__(self, sounds, menu):
		self.menu=menu
		self.sounds=sounds
		self.bonusType=0
		self.bonusAnim=0
		self.font = pygame.font.Font(None,64)
		self.bonusList = list()
		self.bonusList.append(self.font.render(str("plasma gun !"), True, (255,255, 0)))
		self.score=0
		self.bonuscount=1
		
	def ProcessBonus(self, ship):
		#if ship.score %200 ==0 and ship.weapon==1 and ship.score>0:
		
		if ship.score>400*self.bonuscount and self.score<400*self.bonuscount:
			self.menu.play_sound(self.sounds["plasmagun.wav"])
			ship.setWeapon(2)
			self.bonusType=0
			self.bonusAnim=30
			self.score=ship.score
			self.bonuscount=self.bonuscount+1
		
		if self.bonusAnim>0 :
			self.bonusAnim=self.bonusAnim-1
			#show bonus for the plasma weapon
			if self.bonusType==0:
				screen.blit(self.bonusList[0], (250,250 ))
				
				
				
