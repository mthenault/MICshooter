#w : image width
#h : image height
#filename :name of the file
import os
import common_pygame
import pygame, sys, pygame.mixer
from pygame.locals import *

pygame = common_pygame.pygame
screen= common_pygame.screen
clock = common_pygame.clock

class Menu():
	
	
	def __init__(self, single_sprites, sounds, background):
		self.single_sprites=single_sprites
		self.sounds=sounds
		self.background=background
		self.clock=clock
		#1: play
		#2: options
		#3: quit
		self.selection=1
		self.compteur=31
		#0: main menu
		#1: option menu
		self.menuStatus=0
		
		
		
	#start the menu
	#withresume: do we print a resume option ?
	def launch(self, withresume):
		decaly=0
		decalx=-150
		space=120
		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			self.clock.tick_busy_loop(30)
			self.background.updatecompteur()
			screen.fill((0,0,0))
			self.background.blitStars()
			self.background.blitPlanets()
			#show the fog
			self.background.blitFog()
			
			screen.blit(self.single_sprites['menu_micshooter.png'],(120,40))
			
			self.compteur=self.compteur+1


		
			
			
			
			if self.menuStatus==0:
				#change the selection
				if pygame.key.get_pressed()[pygame.K_UP]:
					if self.compteur>=5:
						#print(self.selection)
						self.selection=self.selection-1
						if self.selection==0:
							self.selection=3
						self.compteur=0
						
				if pygame.key.get_pressed()[pygame.K_DOWN] and self.compteur>=5:
					#print(self.selection)
					self.selection=self.selection+1
					if self.selection==4:
						self.selection=1
					self.compteur=0
				
				
				if pygame.key.get_pressed()[pygame.K_RETURN] and self.selection==1:
						return 
						
				if pygame.key.get_pressed()[pygame.K_RETURN] and self.selection==3:
						exit()
						
				if pygame.key.get_pressed()[pygame.K_RETURN] and self.selection==2:
						self.menuStatus=1
				#print the menu accordingly to the selection and the menu state
										
						
				if withresume==0:
					if pygame.key.get_pressed()[K_ESCAPE]:
						exit()
					if self.selection==1:
						if self.compteur<30 and self.compteur%2:
							screen.blit(self.single_sprites['lifeBonusLight.png'],(190-33-decalx,180-32-decaly))	
						screen.blit(self.single_sprites['sprite_ship.png'],(190-decalx,180-decaly))
						
						screen.blit(self.single_sprites['menu_playblurry.png'],(270-decalx,200-decaly))
					else:
						screen.blit(self.single_sprites['menu_play.png'],(270-decalx,200-decaly))
				else:
					if self.selection==1:
						if self.compteur<30 and self.compteur%2:
							screen.blit(self.single_sprites['lifeBonusLight.png'],(190-33-decalx,180-32-decaly))	
						screen.blit(self.single_sprites['sprite_ship.png'],(190-decalx,180-decaly))
						
						screen.blit(self.single_sprites['menu_resumeblurry.png'],(270-decalx,200-decaly))
					else:
						screen.blit(self.single_sprites['menu_resume.png'],(270-decalx,200-decaly))
						
				if self.selection==2:
					if self.compteur<30 and self.compteur%2:
						screen.blit(self.single_sprites['lifeBonusLight.png'],(190-33-decalx,180-32+space-decaly))	
					screen.blit(self.single_sprites['sprite_ship.png'],(190-decalx,180+space-decaly))
						
					screen.blit(self.single_sprites['menu_optionsblurry.png'],(270-decalx,200+space-decaly))
				else:
					screen.blit(self.single_sprites['menu_options.png'],(270-decalx,200+space-decaly))
				
				if self.selection==3:
					if self.compteur<30 and self.compteur%2:
						screen.blit(self.single_sprites['lifeBonusLight.png'],(190-33-decalx,180-32+(2*space)-decaly))	
					screen.blit(self.single_sprites['sprite_ship.png'],(190-decalx,180+(2*space)-decaly))
						
					screen.blit(self.single_sprites['menu_quitblurry.png'],(270-decalx,200+(2*space)-decaly))	
				else:
					screen.blit(self.single_sprites['menu_quit.png'],(270-decalx,200+(2*space)-decaly))
	
			elif self.menuStatus==1:
				screen.blit(self.single_sprites['menu_sound.png'],(270,200))
				
				if pygame.key.get_pressed()[K_ESCAPE]:
					self.menuStatus=0
	
			pygame.display.flip()
	
	#normal laser
