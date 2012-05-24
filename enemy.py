import common_pygame
import collisions
import random
pygame = common_pygame.pygame

class Enemy():
	
	whentoshoot = 0
	nbAsteroids = 0
	def __init__(self, single_sprites, sprite_sequences,sounds, x, y, movementdirection, typeofship):
		self.x = x
		self.y = y
		self.single_sprites=single_sprites
		self.typeofship = typeofship
		
		#this enemy is a ship
		if self.typeofship==0:
			self.sprite_enemy = single_sprites['sprite_enemy.png']
			self.sprite_explosion_list = sprite_sequences['sprite_explosion_list.png']
			self.speed=1
		#this enemy is an asteroid
		else:
			#load the appropriate sprite
			choix = random.randrange(1,4)
			size = random.randrange(80, 100)
			self.y=-size
			if choix ==1:
				self.sprite_enemy = pygame.transform.scale(self.single_sprites['asteroid1.png'], (size , size )).convert_alpha()
			elif choix==2:
				self.sprite_enemy = pygame.transform.scale(self.single_sprites['asteroid3.png'], (size , size )).convert_alpha()				
			else:
				self.sprite_enemy = pygame.transform.scale(self.single_sprites['asteroid2.png'], (size , size )).convert_alpha()
			Enemy.nbAsteroids=Enemy.nbAsteroids+1
			self.speed=3	
			self.sprite_explosion_list = sprite_sequences['sprite_explosion_list_asteroid.png']
		
			#if we are going to be a bonus, what bonus will it be ?
			#0 : health
			#1 : armor
			self.bonusType=bool(random.getrandbits(1))
			if self.bonusType==0:
				self.sprite_bonus=single_sprites['lifebonus.png']
			else:
				self.sprite_bonus=single_sprites['armorbonus.png']
		self.bonus=False
		
			
		
		self.alive = True
		self.dying = False
		self.dying_index=0
		self.screen = common_pygame.screen
		self.sounds= sounds
		self.life = 100
		if movementdirection == 0:
			self.direction=1
		else:
			self.direction=-1
		
		self.compteurx=0
		self.compteury=0
		

		
		self.w = self.sprite_enemy.get_width()
		self.h = self.sprite_enemy.get_height()
		
		Enemy.whentoshoot=Enemy.whentoshoot+1
		self.whentoshoot=((Enemy.whentoshoot)%8)*7
		
		self.laserlist=list()
		self.lasercompteur=self.whentoshoot
		
		#to know when to allow the dead enemy to be purged
		self.timeofdeath=0
		
		#to know if we have to blit the shot sprites
		self.shot=0
		
		
		
		
		

	#are we getting hit ?
	def processHit(self,laserlist, ship):
		oldlasers=list()
		
		
		#is the ship getting the bonus ?	
		if self.bonus:
			if collisions.iscollision(ship.position_ship_x, ship.position_ship_y,
			ship.width, ship.height, self.x, self.y, self.sprite_bonus.get_width(),
			self.sprite_bonus.get_height()):	
				if self.bonusType==0:
					ship.getBonusLife()
				else:
					ship.getBonusArmor()
				self.bonus=False
				self.dying=False
				self.alive=False
		
		#is the ship colliding with the enemy ?
		elif (self.dying == False):
			#check if we collide with the ship. if we collide both looses life
			if collisions.iscollision(ship.position_ship_x, ship.position_ship_y,
			 ship.width, ship.height, self.x, self.y, self.sprite_enemy.get_width(),
			self.sprite_enemy.get_height()):
				if (ship.damage(10)):
					self.life = self.life-150
					if self.life<=0:
						self.dying=True
						if self.typeofship==0:
							self.sounds['explosion.wav'].play()
						else:
							self.sounds['explosion2.wav'].play()
							Enemy.nbAsteroids=Enemy.nbAsteroids-1
							print("dying")
								
						#ship.hurt=True
					ship.position_ship_y=ship.position_ship_y-ship.currentspeed_y
					ship.position_ship_x= ship.position_ship_x-ship.currentspeed_x
					ship.currentspeed_x=-ship.currentspeed_x/1.5
					ship.currentspeed_y=-ship.currentspeed_x/1.5


					
				
			
			#check if we are being shot by a laser
			for index in range(len(laserlist)):
				(currentx, currenty) = laserlist[index]
				if currenty > self.y - self.sprite_enemy.get_height() and \
				currenty < self.y and \
				currentx > self.x and currentx < self.x + self.sprite_enemy.get_width():
					#enemy ship
					if self.typeofship==0:
						self.life=self.life-50
						if self.life<=0:
							self.dying=True
							ship.score=ship.score+10
							self.sounds['explosion.wav'].play()
						else:
							self.shot=30
							self.sounds["shield1.wav"].play()
					else:
						self.dying = True
						ship.score=ship.score+10
						self.sounds['explosion2.wav'].play()
						print("dying")
						Enemy.nbAsteroids=Enemy.nbAsteroids-1
					oldlasers.append((currentx, currenty))
					
		return oldlasers
	
	#blit the correct frame connected with the status
	def update(self, ship):
		#if dying, blit the explosion frame
		if self.dying:
			if self.dying_index/2<len(self.sprite_explosion_list):
				#/2 for one frame every two ticks
				#print("blitting", self.dying_index/2)
				self.screen.blit(self.sprite_explosion_list[(self.dying_index/2)],
				 (self.x-60,
				  self.y-60))
				self.dying_index = self.dying_index +1
			else:
				if (self.typeofship==1):
					self.bonus=True
					self.alive = True
					#Enemy.nbAsteroids=Enemy.nbAsteroids-1
				else:
					self.dying = False
					self.alive = False

		elif self.alive:
			#if we are being shot, there is alternate blitting for one second
			if self.shot>0:
				self.shot=self.shot-1
				if self.shot%2:
					self.screen.blit(self.sprite_enemy, (self.x, self.y))
			else:
				self.screen.blit(self.sprite_enemy, (self.x, self.y))
	
		if self.bonus:
			self.screen.blit(self.sprite_bonus, (self.x, self.y))
			
			
			
		if self.alive:
			#update the position
			if self.y > self.screen.get_width():
				self.dying=False
				self.alive=False
				if (self.typeofship==1):
					Enemy.nbAsteroids=Enemy.nbAsteroids-1
			else:
				if (self.compteurx%120<60):
					self.x = self.x+2*self.direction
				else:
					self.x = self.x-2*self.direction
				self.compteurx=self.compteurx+1
				self.y=self.y+self.speed
				
				#only if we are an enemy ship ( not if asteroid)
				if self.typeofship==0:
					#shooting out a laser 
					if self.lasercompteur==0:
						self.laserlist.append((self.x+self.w/2, self.y+self.h))
						self.lasercompteur=60
						self.sounds["laser4.wav"].play()
						
					#print(self.lasercompteur)
					self.lasercompteur=self.lasercompteur-1
					
					#updating shot lasers
					for index in range(len(self.laserlist)):
						(x, y) = self.laserlist[index]
						self.laserlist[index]=(x, y+10)
						self.screen.blit(self.single_sprites['sprite_laser_blue.png'],(x,y-10))
						#is the ship getting hit by one of our lasers ?
						if collisions.iscollision(x, y, 
						self.single_sprites['sprite_laser_blue.png'].get_width(),
						self.single_sprites['sprite_laser_blue.png'].get_height(), 
						ship.position_ship_x, ship.position_ship_y,  ship.width, 
						ship.height ):
							ship.damage(10)
		
		#if (self.alive==False):
			#self.timeofdeath=self.timeofdeath+1
				
		
##functions that are used in the game loop (TODO : put in another file)
#def reset_speed():
	#currentspeed_x =0
	#currentspeed_y= 0
	#return
