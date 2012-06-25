#w : image width
#h : image height
#filename :name of the file
import os
import common_pygame
import pygame, sys, pygame.mixer
from pygame.locals import *
import pickle
import effects
pygame = common_pygame.pygame
screen= common_pygame.screen
clock = common_pygame.clock

class Menu():
	
	def play_sound(self, sound):
		if self.config['sound']:
			sound.play()
		
	def __init__ (self):
		self.config={}
		if os.path.exists(os.path.join('data','config.conf')):
			with open(os.path.join('data','config.conf'), 'rb') as fichier:
				depickler = pickle.Unpickler(fichier)
				self.config= depickler.load()
		else:
			self.config = {
			"sound" : 1,
			"resolution" : 0}
		
		if self.config['resolution']==0:
			common_pygame.pygame.display.set_mode((800,600))
			common_pygame.screenheight=600
		else:
			common_pygame.pygame.display.set_mode((800,500))
			common_pygame.screenheight=500
        
      #  self.menustatus=0

	def init2(self, single_sprites, sounds, background, hud):
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
		self.menustatus=0
		self.font = pygame.font.Font(None,32)
		self.littlefont = pygame.font.Font(None,25)
        #self.config={}
		self.hud=hud
	#	if self.config['resolution']==0:
	#		self.hud.offset=0
	#	else:
	#		self.hud.offset=100
		

								
							
		#self.sound=1
		##0:800600, 1: 800500
		#self.resolution=0
		
		
	#start the menu
	#withresume: do we print a resume option ?
	def launch(self, withresume):
		decaly=0
		decalx=-150
		space=120
		
		firstRound=True
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
			
			
			
			if self.menustatus==0:
				
				#blit the help
				s = pygame.Surface((300,300))  # the size of your rect
				s.set_alpha(64)                # alpha level
				s.fill((255, 255, 255))           # this fills the entire surface
				screen.blit(s, (25,150))    # (0,0) are the top-left coordinates
				screen.blit(self.littlefont.render("Use the arrow keys and enter", \
				True, (255,255, 255)),(30,155))
				screen.blit(self.littlefont.render("to navigate the menu. ", \
				True, (255,255, 255)),(30,175))
				screen.blit(self.littlefont.render("Game controls : ", \
				True, (255,128, 128)),(30,210))
				screen.blit(self.littlefont.render("Arrow keys : move your ship ", \
				True, (255,255, 255)),(30,230))
				screen.blit(self.littlefont.render("space : fire ", \
				True, (255,255, 255)),(30,250))
				
				if pygame.key.get_pressed()[pygame.K_RETURN] and self.selection==1 and self.compteur>=5:
						self.compteur=0
						effects.fadeToColor(0, 0, 0)
						return 
						
				if pygame.key.get_pressed()[pygame.K_RETURN] and self.selection==3 and self.compteur>=5:
						self.compteur=0
						exit()
						
				if pygame.key.get_pressed()[pygame.K_RETURN] and self.selection==2 and self.compteur>=5:
						self.compteur=0
						self.selection=1
						self.menustatus=1
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
	
			elif self.menustatus==1:

				if (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]) \
				and self.selection==1 and self.compteur>=5:
						self.compteur=0
						self.config['sound']= not self.config['sound']
						
				if (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]) \
				and self.selection==2 and self.compteur>=5:
						self.compteur=0
						self.config['resolution']= not self.config['resolution']
						if self.config['resolution']==0:
							self.hud.offset=0
							common_pygame.pygame.display.set_mode((800,600))
							common_pygame.screenheight=600
						else:
							self.hud.offset=100
							common_pygame.pygame.display.set_mode((800,500))
							common_pygame.screenheight=500
						
				if pygame.key.get_pressed()[pygame.K_RETURN] and self.selection==3:
					#write the config into the file
					with open(os.path.join('data','config.conf'), 'wb') as fichier:
						mon_pickler = pickle.Pickler(fichier)
						mon_pickler.dump(self.config)
						
						self.compteur=0
						self.selection=1
						self.menustatus=0
				
				
				if self.config['sound']:
					if self.selection==1:
						screen.blit(self.font.render("Sound : on", True, (255,0, 0)),(350,200))
					else:
						screen.blit(self.font.render("Sound : on", True, (255,255, 255)),(350,200))
				else:
					if self.selection==1:
						screen.blit(self.font.render("Sound : off", True, (255,0, 0)),(350,200))
					else:
						screen.blit(self.font.render("Sound : off", True, (255,255, 255)),(350,200))
				
				
				if self.config['resolution']==0:
					if self.selection==2:
						screen.blit(self.font.render("Resolution : 800*600", True, (255,0, 0)),(350,250))
					else:
						screen.blit(self.font.render("Resolution : 800*600", True, (255,255, 255)),(350,250))
				else:
					if self.selection==2:
						screen.blit(self.font.render("Resolution : 800*500", True, (255,0, 0)),(350,250))
					else:
						screen.blit(self.font.render("Resolution : 800*500", True, (255,255, 255)),(350,250))
				
				if self.selection==3:
					screen.blit(self.font.render("go back", True, (255,0, 0)),(350,300))
				else:
					screen.blit(self.font.render("go back", True, (255,255, 255)),(350,300))
					
				if pygame.key.get_pressed()[K_ESCAPE]:
					self.menustatus=0
	
			pygame.display.flip()
	
	#normal laser
