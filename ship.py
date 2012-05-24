import os
import common_pygame
pygame = common_pygame.pygame
screen= common_pygame.screen

class Ship():
	
	
	def __init__(self, single_sprites, sounds):
		self.sounds=sounds
		self.sprite=  single_sprites['sprite_ship.png']
		self.single_sprites = single_sprites
		self.height = self.sprite.get_height() 
		self.width =  self.sprite.get_width() 
		self.currentspeed_x =0
		self.currentspeed_y= 0
		self.position_ship_y = screen.get_height()-self.height-64
		self.position_ship_x = screen.get_width()/2 - self.width/2

		self.life = 100
		self.hurt=False
		self.bonus = False
		self.bonustype=0
		self.countdownBonusLife=0
		
		#initial score
		self.score=0
		
		#initial armor
		self.armor=100
	
	def damage (self, amount):
		if self.hurt==False:
			#if we still have armor available
			if self.armor>0:
				self.sounds["shield1.wav"].play()
				self.armor = self.armor-amount
				if self.armor<0:
					self.armor=0
				self.hurt=True
				return True
			#if no more armor, life goes down
			else:
				self.sounds["ouch.wav"].play()
				self.life = self.life-amount
				self.hurt=True
				return True #damage has been effectively inflicted	
		return False #there was no damage
		
	def getBonusLife(self):
		self.score=self.score+5
		self.sounds["life.wav"].play()
		if self.life<100:
			self.life = self.life+10
		self.bonus=True
		self.bonustype=0
		self.countdownBonusLife=0
	
	def getBonusArmor(self):
		self.score=self.score+5
		self.sounds["armor.wav"].play()
		if self.armor<100:
			self.armor = self.armor+10
		self.bonus=True
		self.bonustype=1
		self.countdownBonusLife=0		
		
	def processHurt(self,countdown):
		if self.hurt == True and countdown > 30:
			self.hurt=False
			countdown=0
		elif self.hurt == True:
			countdown = countdown+1
		return countdown
	
	
	def updatePosition(self):
			#update de position X:
		if self.position_ship_x+self.currentspeed_x>screen.get_width()-self.width:
			self.position_ship_x = screen.get_width()-self.width
			#reset the speed
			self.currentspeed_x =0
			self.currentspeed_y= 0
		elif self.position_ship_x+self.currentspeed_x<0:
			self.position_ship_x = 0
			#reset the speed
			self.currentspeed_x =0
			self.currentspeed_y= 0
		else:
			self.position_ship_x = self.position_ship_x + self.currentspeed_x
		
		#update de position Y:
		if self.position_ship_y+self.currentspeed_y>screen.get_height()-self.height:
			self.position_ship_y = screen.get_height()-self.height
			#reset the speed
			self.currentspeed_x =0
			self.currentspeed_y= 0
		elif self.position_ship_y+self.currentspeed_y<0:
			self.position_ship_y = 0
			#reset the speed
			self.currentspeed_x =0
			self.currentspeed_y= 0
		else:
			self.position_ship_y = self.position_ship_y + self.currentspeed_y
			
			
		self.countdownBonusLife = self.countdownBonusLife +1
		if self.bonus == True and self.countdownBonusLife > 50:
			self.bonus=False
			self.countdownBonusLife=0
		elif self.bonus == True:
			self.countdownBonusLife = self.countdownBonusLife+1
			
			
	def blit(self, compteur):
		if self.bonus:
			screen.blit(self.sprite,(self.position_ship_x,self.position_ship_y))
			if compteur%2==0:
				if self.bonustype==0:
					screen.blit(self.single_sprites['lifeBonusRing.png'],(self.position_ship_x,self.position_ship_y))
				else:
					screen.blit(self.single_sprites['armorBonusRing.png'],(self.position_ship_x,self.position_ship_y))
		elif self.hurt:
			if compteur%2==0:
				screen.blit(self.sprite,(self.position_ship_x,self.position_ship_y))
		#el
		else:
			screen.blit(self.sprite,(self.position_ship_x,self.position_ship_y))
	
