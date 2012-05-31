import os
import common_pygame
import load_resources
pygame = common_pygame.pygame
screen= common_pygame.screen

class Ship():
	
	
	def __init__(self, single_sprites, sounds, menu):
		self.menu=menu
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
		
		#initial weapon
		#1: normal laser
		#2: plasma balls
		self.ammo=0
		self.weapon=1
		
	def shoot(self, laserlist, compteur_shoot, laser_width, laser_height, lasershoot):
	#normal laser
		if compteur_shoot>7 and self.weapon == 1:
			self.menu.play_sound(self.sounds['laser.wav'])
			#self.sounds['laser.wav'].play()
			laserlist.append( (self.position_ship_x+self.width/2 -laser_width/2 ,
			self.position_ship_y-laser_height, 1))
			lasershoot = 7
			compteur_shoot=0	
		#plasma balls				
		elif compteur_shoot>2 and self.weapon == 2:
			self.ammo=self.ammo-1
			
			self.menu.play_sound(self.sounds['plasma1.wav'])
			#pygame.mixer.Channel(31).play(self.sounds['plasma1.wav'], 0, 0, 0)
			
			#alternative left/right fire
			if self.ammo%2:
				laserlist.append( (self.position_ship_x+self.width/2 -laser_width/2 -35,
				self.position_ship_y-laser_height+24, 2))
			else:
				laserlist.append( (self.position_ship_x+self.width/2 -laser_width/2 +25,
				self.position_ship_y-laser_height+24, 2))
			#lasershoot = 7
			compteur_shoot=0	
			
		return (compteur_shoot, laserlist, lasershoot) 
			
	def setWeapon (self,  number ):
		if number==1:
			self.weapon=1
			self.sprite=self.single_sprites['sprite_ship.png']
		else:
			self.weapon=2
			self.sprite=self.single_sprites['sprite_ship_weapon2.png']
			self.ammo=100
	
	def damage (self, amount):
		if self.hurt==False:
			#if we still have armor available
			if self.armor>0:
				self.menu.play_sound(self.sounds["shield1.wav"])
				self.armor = self.armor-amount
				if self.armor<0:
					self.armor=0
				self.hurt=True
				return True
			#if no more armor, life goes down
			else:
				self.menu.play_sound(self.sounds["ouch.wav"])
				self.life = self.life-amount
				self.hurt=True
				return True #damage has been effectively inflicted	
		return False #there was no damage
		
	def getBonusLife(self):
		self.score=self.score+5
		self.menu.play_sound(self.sounds["life.wav"])
		if self.life<100:
			self.life = self.life+10
		self.bonus=True
		self.bonustype=0
		self.countdownBonusLife=0
	
	def getBonusArmor(self):
		self.score=self.score+5
		self.menu.play_sound(self.sounds["armor.wav"])
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
			
		#switch to the main weapon if the current one is empty
		if self.ammo<=0:
			self.setWeapon(1)
			
			
	def blit(self, compteur):
		if self.bonus:
			screen.blit(self.single_sprites['lifeBonusLight.png'],(self.position_ship_x-33,self.position_ship_y-32))
			screen.blit(self.sprite,(self.position_ship_x,self.position_ship_y))
			if compteur%2==0:
				if self.bonustype==0:
					screen.blit(self.single_sprites['lifeBonusRing.png'],(self.position_ship_x,self.position_ship_y))
				else:
					screen.blit(self.single_sprites['armorBonusRing.png'],(self.position_ship_x,self.position_ship_y))
		elif self.hurt:
			if compteur%2==0:
				screen.blit(self.single_sprites['sprite_ship_fire.png'],(self.position_ship_x,self.position_ship_y+61))
				screen.blit(self.sprite,(self.position_ship_x,self.position_ship_y))
		#el
		else:
			screen.blit(self.single_sprites['sprite_ship_fire.png'],(self.position_ship_x,self.position_ship_y+61))
			screen.blit(self.sprite,(self.position_ship_x,self.position_ship_y))
	
