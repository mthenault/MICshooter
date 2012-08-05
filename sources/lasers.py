import common_pygame
import collisions
import random
pygame = common_pygame.pygame
screen= common_pygame.screen

class Lasers():
	#init the laser object
	def __init__(self, single_sprites, ship):
		self.laserlist = list()
		self.single_sprites= single_sprites
		self.ship = ship
	#adding a laser to the list
	def addLaser(self, x, y ):
		self.laserlist.append((x, y))



	def update(self):
		#updating shot lasers
		tmplist = list()
		for index in range(len(self.laserlist)):
			(x, y) = self.laserlist[index]
			self.laserlist[index]=(x, y+10)
			screen.blit(self.single_sprites['sprite_laser_blue_light.png'],(x-29-32,y-10-22-32))
			screen.blit(self.single_sprites['sprite_laser_blue.png'],(x,y-10))
			#is the ship getting hit by one of our lasers ?
			
			if collisions.iscollision(x, y, 
			self.single_sprites['sprite_laser_blue.png'].get_width(),
			self.single_sprites['sprite_laser_blue.png'].get_height(), 
			self.ship.position_ship_x, self.ship.position_ship_y,  self.ship.width, 
			self.ship.height ):
				self.ship.damage(10, x-40)
				tmplist.append(self.laserlist[index])
		
		#and we delete the old lasers
		for index in range(len(tmplist)):
			self.laserlist.remove(tmplist[index])	
