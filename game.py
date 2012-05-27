#!/usr/bin/env python
import pygame, sys, pygame.mixer
from pygame.locals import *
import common_pygame
import enemy
import load_resources
import random
import ship
import background
import hud
import bonus

pygame = common_pygame.pygame
screen= common_pygame.screen
clock = common_pygame.clock



#dictionnaries that will contain all our needed resources
sounds = dict()
single_sprites = dict()
sprite_sequences = dict()

#fill up our dictionnaries
(sounds, single_sprites, sprite_sequences) = load_resources.load_resources(pygame)

#sprite proprieties being used later
laser_height = single_sprites['sprite_laser.png'].get_height()
laser_width = single_sprites['sprite_laser.png'].get_width()
lasershoot_width =  single_sprites['sprite_lasershoot.png'].get_width()
lasershoot_height =  single_sprites['sprite_lasershoot.png'].get_height()


laserlist = list()

lasershoot = 7

tinyfont = pygame.font.Font(None, 16)
font = pygame.font.Font(None,32)
font2 = pygame.font.Font(None, 150)

ship = ship.Ship(single_sprites, sounds )
ship.setWeapon(1)

#bonus processing
scoreBonus=bonus.Bonus(sounds)

hud= hud.Hud(single_sprites)
#ship.height = single_sprites['sprite_ship.png'].get_height() 
#ship.width =  single_sprites['sprite_ship.png'].get_width() 
#ship.currentspeed_x =0
#ship.currentspeed_y= 0

#ship.position_ship_y = screen.get_height()-ship.height-64
#ship.position_ship_x = screen.get_width()/2 - ship.width/2

#ship.life = 100
#ship.hurt=False
ship_top = screen.get_height()-ship.height
ship_left = screen.get_width()/2 - ship.width/2

decal_laser_ship_x = (ship.width /2)
coord_laser_ship_y = -40

#mspawner = Spawner()s
#list
#create 10 enemies
enemy_list = list()

compteur = 0
countdown=0
#to know if it's ok to shoot
compteur_shoot=int(0)
nbAsteroids=0
#current_sprite=0

it=0
background = background.BackGen(single_sprites)
thegame=True
level =1
while thegame:
	compteur_shoot=compteur_shoot+1
	#level 1 : 3 enemies every 3 seconds
	if level==1:
		if compteur%(3*60)==0:
			
			boolrand = bool(random.getrandbits(1))
			for i in range(3):
				enemy_list.append(enemy.Enemy( single_sprites, sprite_sequences , sounds,
				i*80+250+60*int(boolrand), -single_sprites['sprite_enemy.png'].get_height(),boolrand , 0))
			print (enemy_list[0].nbAsteroids)
	
	#new asteroids
	#if ((len(enemy_list)==0) or enemy_list[0].nbAsteroids<=2) and compteur%150==0:
	if compteur%150==0:
		boolrand = bool(random.getrandbits(1))
		enemy_list.append(enemy.Enemy( single_sprites, sprite_sequences , sounds,
			random.randrange(0, screen.get_width()), -32,boolrand , 1))
		enemy_list[0].nbAsteroids=enemy_list[0].nbAsteroids+1
		#if (len(enemy_list)>=0):
			#print(
			
	compteur = compteur +1 
	background.updatecompteur()
	
	
	clock.tick_busy_loop(30)
	screen.fill((0,0,0))

	#blit the stars and the asteroids
	background.blitStars()
	background.blitPlanets()
		#show the fog
	background.blitFog()
	#screen.blit(single_sprites['background.png'],(0,-600+(compteur%150*4)))
	#screen.blit(single_sprites['background.png'],(0,compteur%150*4))

	
	mouse_x,mouse_y=pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#elif event.type == MOUSEBUTTONDOWN:
			#sounds['laser.wav'].play()
			#laserlist.append( (ship.position_ship_x+ship.width/2 -laser_width/2 ,
			#ship.position_ship_y-laser_height))
			#lasershoot = 7
					
	if pygame.key.get_pressed()[K_LEFT]:
		ship.currentspeed_x = ship.currentspeed_x -1 

	if pygame.key.get_pressed()[K_LEFT]:
		ship.currentspeed_x = ship.currentspeed_x -1 
	elif pygame.key.get_pressed()[K_RIGHT]:
		ship.currentspeed_x = ship.currentspeed_x +1 		
	if pygame.key.get_pressed()[K_DOWN]:
		ship.currentspeed_y = ship.currentspeed_y +1 
	elif pygame.key.get_pressed()[K_UP]:
		ship.currentspeed_y = ship.currentspeed_y -1 	
	
	#are we shooting ?
	if pygame.key.get_pressed()[K_SPACE]:
		(compteur_shoot, laserlist, lasershoot) =ship.shoot(laserlist,compteur_shoot, laser_width, laser_height, lasershoot)
		
				
	#update the ships position
	ship.updatePosition()
	#blit the right thing
	ship.blit(compteur)
			
	
	
	#blit the laser shot fire
	if lasershoot >= 0 :
		screen.blit(single_sprites['sprite_lasershoot.png'],(ship.position_ship_x+ship.width/2 -lasershoot_width/2,
		 ship.position_ship_y ))
		lasershoot = lasershoot -1
		
	oldLasers = list()	
	#blit the lasers
	for index in range(len(laserlist)):
		(currentx, currenty, lasertype) = laserlist[index]
		if currenty>=-40:
			#it's a normal laser
			if lasertype==1:
				screen.blit(single_sprites['sprite_laser_light.png'],(currentx-29-32,currenty-22-32))
				screen.blit(single_sprites['sprite_laser.png'],(currentx,currenty))
				currenty = currenty - 15
			#it's a plasma ball
			else :
				screen.blit(single_sprites['ball1_light.png'],(currentx-10,currenty-10))
				screen.blit(single_sprites['ball1.png'],(currentx,currenty))
				currenty = currenty - 20				
			
			laserlist[index]=(currentx,currenty, lasertype)
		else:
			oldLasers.append((currentx,currenty, lasertype))
	#purge old lasers
	for index in range(len(oldLasers)):
		laserlist.remove(oldLasers[index])
		
	deadEnemies=list()
	#blit and process the enemies
	for index in range(len(enemy_list)):
		oldLasers=enemy_list[index].processHit(laserlist, ship)
		enemy_list[index].update(ship)
		if enemy_list[index].alive==False:
			deadEnemies.append(enemy_list[index])
			#purge old lasers
		for index in range(len(oldLasers)):
			laserlist.remove(oldLasers[index])	
		
	#purge dead enemies
	for index in range(len(deadEnemies)):
		enemy_list.remove(deadEnemies[index])	
			
	#blit the hud		
	hud.blit(ship, level)
			
	#process ship hurt
	countdown = ship.processHurt(countdown)
	
	
	if (ship.life<=0):
		thegame=False
		youlost = font2.render("Loser !", True, (255,255, 255))
		presskey = font.render("press any key to quit", True, (255,255, 255))
	
	scoreBonus.ProcessBonus(ship)
		
	pygame.display.flip()

exitloop = True
exitcountdown =0

while exitloop:
	exitcountdown =exitcountdown+ 1
	clock.tick_busy_loop(30)
	screen.fill((0,0,0))
	
	background.updatecompteur()
	background.blitStars()
	background.blitPlanets()
	#show the fog
	background.blitFog()
	screen.blit(youlost, (250,250 ))
	screen.blit(presskey, (300,350 ))
	if exitcountdown==30:
		sounds["loser.wav"].play()
		
	if exitcountdown>=30:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		if pygame.key.get_pressed()[K_SPACE]:
			print("exiting")
			exit()
			exitloop=False

	#if pygame.KEYDOWN:
		#print("exiting")
		#exit()
	pygame.display.flip()
	
