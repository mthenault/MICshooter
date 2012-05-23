#!/usr/bin/env python
import pygame, sys, pygame.mixer
from pygame.locals import *
import common_pygame
import enemy
import load_resources
import random
import ship
import background

pygame = common_pygame.pygame
screen= common_pygame.screen
clock = common_pygame.clock

# Create a font
font = pygame.font.Font(None, 32)
font2 = pygame.font.Font(None, 150)

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

##our ship
#class Ship:
    #pass

ship = ship.Ship(single_sprites, sounds )
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
while thegame:
	compteur_shoot=compteur_shoot+1
	#new enemies every 3 seconds
	if compteur%(3*60)==0:
		
		boolrand = bool(random.getrandbits(1))
		for i in range(8):
			enemy_list.append(enemy.Enemy( single_sprites, sprite_sequences , sounds,
			i*80+30+60*int(boolrand), 0,boolrand , 0))
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
	
	if pygame.key.get_pressed()[K_SPACE]:
		if compteur_shoot>5:
			sounds['laser.wav'].play()
			laserlist.append( (ship.position_ship_x+ship.width/2 -laser_width/2 ,
			ship.position_ship_y-laser_height))
			lasershoot = 7
			compteur_shoot=0							

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
		(currentx, currenty) = laserlist[index]
		if currenty>=-40:
			screen.blit(single_sprites['sprite_laser.png'],(currentx,currenty))
			currenty = currenty - 15
			laserlist[index]=(currentx,currenty)
		else:
			oldLasers.append((currentx,currenty))
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
			
					
	#process ship hurt
	countdown = ship.processHurt(countdown)
	

	#screen.blit(single_sprites['backgroundtransp.png'],(0,-600+(compteur%40*15)))
	#screen.blit(single_sprites['backgroundtransp.png'],(0,compteur%40*15))
	
	# Render the text
	text = font.render("Life: "+str(ship.life)+"%", True, (255,
	255, 255))
	# Create a rectangle
	#textRect = text.get_rect()
	#show the HUD
	screen.blit(text, (common_pygame.screenwidth-120,common_pygame.screenheight-230 ))
		
	#if compteur%2== 0:
		#current_sprite = current_sprite +1
		#print("current sprite", current_sprite,len(sprite_explosion_list))
		
	#screen.blit(sprite_explosion_list[current_sprite%len(sprite_explosion_list)], (10, 10))
	#ship.life=0
	if (ship.life<=0):
		thegame=False
		youlost = font2.render("Loser !", True, (255,255, 255))
		presskey = font.render("press any key to quit", True, (255,255, 255))
		# Create a rectangle
		#textRect = youlost.get_rect()
		#screen.blit(youlost, (250,250 ))
		#screen.blit(presskey, (300,350 ))
		
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
	
