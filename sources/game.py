#!/usr/bin/env python
def game():
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
	import menu
	import effects
	import particles

	pygame = common_pygame.pygame
	screen= common_pygame.screen
	clock = common_pygame.clock



	#dictionnaries that will contain all our needed resources
	sounds = dict()
	single_sprites = dict()
	sprite_sequences = dict()

	#create the menu ( we create it here in order to let the menu object read the configuration,
	#to set the correct screen size

	menu=menu.Menu()
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

	background = background.BackGen(single_sprites)







	hud= hud.Hud(single_sprites, menu, sounds)
	#start the menu
	menu.init2(single_sprites, sounds, background, hud)
	menu.launch(0)


	ship = ship.Ship(single_sprites, sounds, menu, sprite_sequences )
	ship.setWeapon(1)

	ship_top = screen.get_height()-ship.height
	ship_left = screen.get_width()/2 - ship.width/2

	decal_laser_ship_x = (ship.width /2)
	coord_laser_ship_y = -40


	enemy_list = list()

	compteur = 0
	countdown=0
	#to know if it's ok to shoot
	compteur_shoot=int(0)
	nbAsteroids=0
	#current_sprite=0

	it=0

	#bonus processing
	scoreBonus=bonus.Bonus(sounds, menu)



	thegame=True
	level =-1
	spawnedBoss=False
	while thegame:
		compteur_shoot=compteur_shoot+1
		
		#every 2 minutes, level up
		if compteur%(30*60)==0:
			level=level+1
		#level 1 : 3 enemies every 3 seconds
		if level==1:
			if compteur%(3*20)==0:
				
				boolrand = bool(random.getrandbits(1))
				for i in range(1):
					enemy_list.append(enemy.Enemy( single_sprites, sprite_sequences , sounds,
					i*80+250+60*int(boolrand), -single_sprites['sprite_enemy.png'].get_height(),boolrand , 0, menu))
				print (enemy_list[0].nbAsteroids)
		if level==2:
			if compteur%(2*60)==0:
				
				boolrand = bool(random.getrandbits(1))
				for i in range(6):
					enemy_list.append(enemy.Enemy( single_sprites, sprite_sequences , sounds,
					i*80+190+60*int(boolrand), -single_sprites['sprite_enemy.png'].get_height(),boolrand , 0, menu))
				print (enemy_list[0].nbAsteroids)
		if level==3 and not spawnedBoss:
			enemy_list.append(enemy.Enemy( single_sprites, sprite_sequences , sounds, 
			400-single_sprites['boss1.png'].get_width()/2, -single_sprites['boss1.png'].get_height(),1 , 2, menu))
			spawnedBoss=True
			#if compteur%(1*60)==0:
				
				#boolrand = bool(random.getrandbits(1))
				#for i in range(9):
					#enemy_list.append(enemy.Enemy( single_sprites, sprite_sequences , sounds,
					#i*80+80+60*int(boolrand), -single_sprites['sprite_enemy.png'].get_height(),boolrand , 0, menu))
				#print (enemy_list[0].nbAsteroids)
				
		#new asteroids
		#if ((len(enemy_list)==0) or enemy_list[0].nbAsteroids<=2) and compteur%150==0:
		if compteur%150==0:
			boolrand = bool(random.getrandbits(1))
			enemy_list.append(enemy.Enemy( single_sprites, sprite_sequences , sounds,
				random.randrange(0, screen.get_width()), -32,boolrand , 1, menu))
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

		
		mouse_x,mouse_y=pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			#elif event.type == MOUSEBUTTONDOWN:
				#sounds['laser.wav'].play()
				#laserlist.append( (ship.position_ship_x+ship.width/2 -laser_width/2 ,
				#ship.position_ship_y-laser_height))
				#lasershoot = 7
		if pygame.key.get_pressed()[K_ESCAPE]:
			#launch menu with resume option
			menu.launch(1) 				
		if pygame.key.get_pressed()[K_LEFT]:
			if ship.currentspeed_x >=0:
				ship.currentspeed_x = -5
			if ship.currentspeed_x > -20:
				ship.currentspeed_x = ship.currentspeed_x -1
			
		elif pygame.key.get_pressed()[K_RIGHT]:
			if ship.currentspeed_x <= 0:
				ship.currentspeed_x = 5
			if ship.currentspeed_x < 20:
				ship.currentspeed_x = ship.currentspeed_x +1
		if pygame.key.get_pressed()[K_DOWN]:
			if ship.currentspeed_y <= 0:
				ship.currentspeed_y = 5
			if ship.currentspeed_y < 20:
				ship.currentspeed_y = ship.currentspeed_y +1
		elif pygame.key.get_pressed()[K_UP]:
			if ship.currentspeed_y >= 0:
				ship.currentspeed_y = -5
			if ship.currentspeed_y > -20:
				ship.currentspeed_y = ship.currentspeed_y -1
		
		if 	pygame.key.get_pressed()[K_LEFT] ==0 and pygame.key.get_pressed()[K_RIGHT]==0 \
		and pygame.key.get_pressed()[K_UP] ==0 and pygame.key.get_pressed()[K_DOWN]==0:
			ship.currentspeed_y=0
			ship.currentspeed_x=0
		
		
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
		level = hud.blit(ship, level)
				
		#process ship hurt
		countdown = ship.processHurt(countdown)

		if (ship.life<=0):
			thegame=False
			youlost = font2.render("Game over", True, (255,255, 255))
			presskey = font.render("press any key to quit", True, (255,255, 255))
			yourscore = font.render("Your score : "+ str(ship.score), True, (255,255, 255))
			
			#play a the explosion sound
			menu.play_sound(sounds['explosion2.wav'])
			#blit the explosion
			screen.blit(sprite_sequences['sprite_explosion_list_asteroid.png'][3],\
			 (ship.position_ship_x-64,ship.position_ship_y-64))
			#fade to red
			effects.fadeToColor(255, 0, 0)
		#scoreBonus.ProcessBonus(ship)
		particles.blitAndUpdate()
		
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
		screen.blit(youlost, (150,50 ))
		screen.blit(yourscore, (250,180 ))
		screen.blit(presskey, (300,450 ))
		
		if exitcountdown==30:
			menu.play_sound(sounds["loser.wav"])
			
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
		
