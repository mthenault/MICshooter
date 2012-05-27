import os
import common_pygame
import random
pygame = common_pygame.pygame
screen= common_pygame.screen

class Bonus():
	def __init__(self, sounds):
		self.sounds=sounds
		self.bonusType=0
		self.bonusAnim=0
		self.font = pygame.font.Font(None,64)
		self.bonusList = list()
		self.bonusList.append(self.font.render(str("plasma gun !"), True, (255,255, 0)))
		
	def ProcessBonus(self, ship):
		if ship.score %500 ==0 and ship.weapon==1 and ship.score>0:
			self.sounds["plasmagun.wav"].play()
			ship.setWeapon(2)
			self.bonusType=0
			self.bonusAnim=30
		
		if self.bonusAnim>0:
			self.bonusAnim=self.bonusAnim-1
			#show bonus for the plasma weapon
			if self.bonusType==0:
				screen.blit(self.bonusList[0], (250,250 ))
				
				
				
