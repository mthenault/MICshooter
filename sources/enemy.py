import common_pygame
import collisions
import random
import hud

pygame = common_pygame.pygame

class Enemy():
	
	whentoshoot = 0
	nbAsteroids = 0
	def __init__(self, single_sprites, sprite_sequences,sounds, x, y, movementdirection, typeofship, menu):
		self.menu=menu
		
		self.x = x
		self.y = y
		self.single_sprites=single_sprites
		self.typeofship = typeofship
		self.sprite_sequences =sprite_sequences
		
	
		#enemy types
		#0 : ship
		#1 : asteroid
		#2 : the first boss
		
		#this enemy is a ship
		if self.typeofship==0:
			self.bonusType=random.randint(0,1)
			
			if bool(random.getrandbits(1)):
				self.sprite_enemy = single_sprites['sprite_enemy.png']
			else:
				self.sprite_enemy = single_sprites['sprite_enemy2.png']
			self.sprite_explosion_list = sprite_sequences['sprite_explosion_list.png']
			self.speed=5
			
			#what is the maximum distance with the players ship ?
			self.distance=random.randrange(1,8)*50
			#what is the maximum distance before turning ?
			self.offsetturn=random.randrange(1,9)*50
			self.life = 100
		#this enemy is an asteroid
		elif self.typeofship==1:
			self.life = 100
			self.bonusType=random.randint(0,2)
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
			
			self.bonusType=random.randint(0,2)
		#this enemy is the first boss
		else:
			self.bossmove=1
			self.bossmoveVertical=1
			self.bossHorizontalSpeed=5
			self.bonusType=random.randint(0,1)
			self.speed=5
			self.sprite_explosion_list = sprite_sequences['sprite_explosion_list.png']
			self.sprite_enemy = single_sprites['boss1.png']
			#what is the maximum distance with the players ship ?
			self.distance=4*50
			#what is the maximum distance before turning ?
			self.offsetturn=600
			self.inPlace=False
			self.life=3000
		
		
		
		#if we are going to be a bonus, what bonus will it be ?
		#0 : health
		#1 : armor
		#2 : plasma
		
		if self.bonusType==0:
			self.sprite_bonus=single_sprites['lifebonus.png']
		elif self.bonusType==1:
			self.sprite_bonus=single_sprites['armorbonus.png']
		else:
			self.sprite_bonus=single_sprites['plasmabonus.png']
		self.bonus=False
		
		self.alive = True
		self.dying = False
		self.dying_index=0
		self.screen = common_pygame.screen
		self.sounds= sounds
		
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
				elif self.bonusType==1:
					ship.getBonusArmor()
				else:
					ship.setWeapon(2)
				self.bonus=False
				self.dying=False
				self.alive=False
		
		#is the ship colliding with the enemy ?
		elif (self.dying == False):
			#check if we collide with the ship. if we collide both looses life
			if collisions.iscollision(ship.position_ship_x, ship.position_ship_y,
			 ship.width, ship.height, self.x, self.y, self.sprite_enemy.get_width(),
			self.sprite_enemy.get_height()):
				if (ship.damage(10, ship.position_ship_x)):
					self.life = self.life-150
					if self.life<=0:
						self.dying=True
						if self.typeofship==0:
							self.menu.play_sound(self.sounds['explosion.wav'])
						else:
							self.menu.play_sound(self.sounds['explosion2.wav'])
							Enemy.nbAsteroids=Enemy.nbAsteroids-1
							print("dying")
								
						#ship.hurt=True
				ship.position_ship_y=ship.position_ship_y-ship.currentspeed_y
				ship.position_ship_x= ship.position_ship_x-ship.currentspeed_x
				ship.currentspeed_x=-ship.currentspeed_x/1.5
				ship.currentspeed_y=-ship.currentspeed_x/1.5


					
				
			
			#check if we are being shot by a laser
			for index in range(len(laserlist)):
				(currentx, currenty, lasertype) = laserlist[index]
				#if currenty > self.y - self.sprite_enemy.get_height() and \
				#currenty < self.y and \
				#currentx > self.x and currentx < self.x + self.sprite_enemy.get_width():
				if lasertype==1:
					(laserX, laserY) = (5, 19)
				else:
					(laserX, laserY) = (12, 12)
					
				if collisions.iscollision(currentx, currenty, laserX, laserY, self.x, \
				 self.y, self.sprite_enemy.get_width(), self.sprite_enemy.get_height()):
					#enemy ship
					if self.typeofship==0:
						self.life=self.life-50
						if self.life<=0:
							self.dying=True
							ship.score=ship.score+10
							self.menu.play_sound(self.sounds['explosion.wav'])
						else:
							self.shot=30
							self.menu.play_sound(self.sounds["shield1.wav"])
					#asteroid
					elif self.typeofship==1:
						self.dying = True
						ship.score=ship.score+10
						self.menu.play_sound(self.sounds['explosion2.wav'])
						#print("dying")
						Enemy.nbAsteroids=Enemy.nbAsteroids-1
					#first boss
					else:
						self.life=self.life-10
						if self.life<=0:
							self.dying=True
							ship.score=ship.score+10
							self.menu.play_sound(self.sounds['explosion.wav'])
						else:
							self.shot=30
							self.menu.play_sound(self.sounds["shield1.wav"])
						
					oldlasers.append((currentx, currenty, lasertype))
					
		return oldlasers
	
	#blit the correct frame connected with the status
	def update(self, ship):
		#if dying, blit the explosion frame
		if self.dying:
			if self.dying_index/2<len(self.sprite_explosion_list):
				#/2 for one frame every two ticks
				#print("blitting", self.dying_index/2)
				self.screen.blit(self.sprite_explosion_list[(self.dying_index/2)],
				 (self.x-112,
				  self.y-86))
				self.dying_index = self.dying_index +1
			else:
				#asteroid
				#if (self.typeofship==1):
				self.bonus=True
				self.alive = True
					#Enemy.nbAsteroids=Enemy.nbAsteroids-1
				#enemy ship
				#else:
				#	self.dying = False
				#	self.alive = False

		elif self.alive:
			#if we are being shot, there is alternate blitting for one second
			if self.shot>0:		
				#explosion
				if 30-self.shot<len(self.sprite_sequences['ship_hurt.png']):
					self.screen.blit(self.sprite_sequences['ship_hurt.png'][30-self.shot], (self.x, self.y+32))
					
				self.shot=self.shot-1
				if self.shot%2:
					if self.typeofship==0:
						self.screen.blit(self.single_sprites['sprite_enemy_fire.png'], (self.x, self.y-15))
					self.screen.blit(self.sprite_enemy, (self.x, self.y))
				##if we are the first boss, we draw the sprite anyway
				#if self.typeofship==2:
					#self.screen.blit(self.sprite_enemy, (self.x, self.y))
			else:
				if self.typeofship==0:
					self.screen.blit(self.single_sprites['sprite_enemy_fire.png'], (self.x, self.y-15))
				self.screen.blit(self.sprite_enemy, (self.x, self.y))
	
		if self.bonus:
			self.y=self.y+5
			self.screen.blit(self.sprite_bonus, (self.x, self.y))
			
			
			
		if self.alive:
			#update the position
			if self.y > self.screen.get_width():
				self.dying=False
				self.alive=False
				if (self.typeofship==1):
					Enemy.nbAsteroids=Enemy.nbAsteroids-1
			else:
				
				#move of a living enemy
				if self.dying==False and self.typeofship==0:
					#update the direction in accordance to the ship's position
					if self.x < ship.position_ship_x and ship.position_ship_x - self.x >self.offsetturn:
						self.direction=1
					elif self.x - ship.position_ship_x >self.offsetturn:
						self.direction=-1
					#move the enemy
					#if self.y > ship.position_ship_y -250:
						#self.y = self.y-20
					elif self.y < ship.position_ship_y -self.distance :
						self.y = self.y+5
						
					self.x = self.x+10*self.direction
					
				#move of an asteroid
				elif self.typeofship==1:
					
					if (self.compteurx%120<60):
						self.x = self.x+5*self.direction
					else:
						self.x = self.x-5*self.direction
						self.y=self.y+self.speed
				
				#move of the first boss	
				if self.typeofship==2 :
					#the first move of the boss before getting into position
					if not self.inPlace:
						if self.y>=100:
							self.inPlace=True
						else:
							self.y=self.y+10
					else:	
						#we continue to go down till we reach a value
						if self.y>=150 or self.y <=20:
							self.bossmoveVertical=- self.bossmoveVertical
						
						self.y=self.y+self.bossmoveVertical
					
						
					#we have to move across all the screen, the speed changes on each turn
					if self.x<=0:
						self.bossmove=1
						self.bossHorizontalSpeed=random.randint(4,10)
					elif self.x>=800-self.w:
						self.bossmove=-1
						self.bossHorizontalSpeed=random.randint(4,10)
					
					self.x=self.x+self.bossmove*self.bossHorizontalSpeed
					
					#if (self.compteurx%200<60):
						#self.x = self.x+5*self.direction
					#else:
						#self.x = self.x-5*self.direction
					
					
				self.compteurx=self.compteurx+1
				
				
				#only if we are an enemy ship ( not if asteroid), and not dying, and not dead 
				if not self.bonus and not self.dying and ( self.typeofship==0 or self.typeofship==2):
					#shooting out a laser 
					if self.lasercompteur==0:
						self.laserlist.append((self.x+self.w/2, self.y+self.h))
						
						#if we are the boss, shoot out the lasers faster
						if self.typeofship==2:
							self.lasercompteur=5
						else:
							self.lasercompteur=60
						self.menu.play_sound(self.sounds["laser4.wav"])
						
					#print(self.lasercompteur)
					self.lasercompteur=self.lasercompteur-1
					
					#updating shot lasers
					tmplist = list()
					for index in range(len(self.laserlist)):
						(x, y) = self.laserlist[index]
						self.laserlist[index]=(x, y+10)
						self.screen.blit(self.single_sprites['sprite_laser_blue_light.png'],(x-29-32,y-10-22-32))
						self.screen.blit(self.single_sprites['sprite_laser_blue.png'],(x,y-10))
						#is the ship getting hit by one of our lasers ?
						
						if collisions.iscollision(x, y, 
						self.single_sprites['sprite_laser_blue.png'].get_width(),
						self.single_sprites['sprite_laser_blue.png'].get_height(), 
						ship.position_ship_x, ship.position_ship_y,  ship.width, 
						ship.height ):
							ship.damage(10, x-40)
							tmplist.append(self.laserlist[index])
					
					#and we delete the old lasers
					for index in range(len(tmplist)):
						self.laserlist.remove(tmplist[index])	
				
				#if we are the boss : shooting out lasers
				#if self.typeofship==2:
		#if we are the first boss, we print the progress bar
		if self.typeofship==2:
			hud.updateProgbar(self.life/30,10, 10,400, (255,0,0), 1)
		
		
		
		
		
		
		
		#if (self.alive==False):
			#self.timeofdeath=self.timeofdeath+1
				
		
##functions that are used in the game loop (TODO : put in another file)
#def reset_speed():
	#currentspeed_x =0
	#currentspeed_y= 0
	#return
