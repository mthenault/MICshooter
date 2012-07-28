import os
import common_pygame
import random
pygame = common_pygame.pygame
screen= common_pygame.screen


	#def __init__(self):
		#self.color=(0, 0, 255)
		#self.y1 = screen.get_height()/2
		#self.y2 = self.y1 +20
		#self.max_width=800-40
		##self.font = pygame.font.Font(None,64)
		
		#self.textHeight=self.y1-80
def negtozero ( x):
	if x<0:
		return 0
	return x
	
def	updateProgbar(percent,x1,  y1,max_width, color, direction, single_sprites):
	s = pygame.Surface((max_width,15))  # the size of your rect
	s.set_alpha(64)                # alpha level
	s.fill(color)           # this fills the entire surface
	screen.blit(s, (x1,y1))    # (0,0) are the top-left coordinates
	
	##txtpercent = self.font.render(str(percent)+"%", True, self.color)
	##screen.blit(txtpercent, (20,y1+30))
	(r, g, b) = color
	if direction==1:
		for i in range((percent*max_width)/100):
			screen.blit(single_sprites['barArmor.png'],(x1+i,y1))
		#	pygame.draw.rect(screen, newcol, (x1,y1+i,(percent*max_width)/100,2), 0)
			
	else:
		for i in range((percent*max_width)/100):
			screen.blit(single_sprites['barLife.png'],(x1+max_width-i,y1))
		#pygame.draw.rect(screen, color, (x1+(max_width-(percent*max_width)/100),y1,(percent*max_width)/100,15), 0)
	#pygame.draw.rect(screen,  color2, (x1,y1,max_width,15), 1 )



class Hud():
	def __init__(self, single_sprites, menu, sounds):
		self.sounds=sounds
		self.menu=menu
		self.single_sprites=single_sprites
			# Create a font
		self.tinyfont = pygame.font.Font(None, 16)
		self.font = pygame.font.Font(None,32)
		self.font2 = pygame.font.Font(None, 150)
		self.score_label = self.tinyfont.render("score", True, (255,255, 0))
		self.inf = self.font.render("Inf.", True, (0,130, 255))
		self.communication = pygame.font.Font("A.TTF",13)
		self.communicationCall = pygame.font.Font("BITSUMIS.TTF",50)
		
		#self.offset=0
		self.johnsonOffset =0
		self.textline1 = "Johnson here."
		self.textline2 = "Your goal today is to destroy"
		self.textline3 = "every enemy ship. "
		self.textline4 = "I'm counting on you !"
	def blit(self, ship, level):
			# Render the text
		#life_txt = self.font.render(str(ship.life), True, (255,0, 0))
		score_txt = self.font.render(str(ship.score), True, (255,255, 255))
		#armor_txt = self.font.render(str(ship.armor), True, (255,255, 0))
		level_txt = self.tinyfont.render("level " + str(level), True, (255,255, 0))
		#show the HUD
		screen.blit(self.single_sprites['lifemask.png'],(0,common_pygame.screenheight
                                                   - self.single_sprites['lifemask.png'].get_height()))
		#show the life and the score
		screen.blit(self.score_label, (680,common_pygame.screenheight-50))
		screen.blit(score_txt, (725,common_pygame.screenheight-55))
		#screen.blit(level_txt, (455,common_pygame.screenheight-215-30 -self.offset))
		
		#print(common_pygame.screenheight)	
		#progress bar for the armor
		updateProgbar(ship.armor,25,  common_pygame.screenheight-23, 150, (7,200,0), 1, self.single_sprites)
		screen.blit(self.single_sprites['armorbonus.png'],(0,common_pygame.screenheight-32))
		
		#progress bar for the life
		updateProgbar(ship.life,common_pygame.screenwidth-25-150,
                common_pygame.screenheight-23, 150, (0,181,200), 0, self.single_sprites)
		screen.blit(self.single_sprites['lifebonus.png'],(common_pygame.screenwidth-25,common_pygame.screenheight-32))		
		
        
		#screen.blit(armor_txt, (35,common_pygame.screenheight-227-self.offset ))
		
		#blit the current weapon and the ammo
		if ship.weapon==1:
			screen.blit(self.single_sprites['sprite_laser.png'],(5,
                                                        common_pygame.screenheight-55))
			screen.blit(self.inf,(25, common_pygame.screenheight-55))
		else:
			ammo_txt = self.font.render(str(ship.ammo), True, (0,130, 255))
			screen.blit(self.single_sprites['ball1.png'],(5,
                                                 common_pygame.screenheight-55 ))
			screen.blit(ammo_txt,(25, common_pygame.screenheight-55))
			
		#beggining of the game : blit johnson
		if level==0:
			if self.johnsonOffset==230:
				return 1
			else:
				self.johnsonOffset=self.johnsonOffset+1
				
				if self.johnsonOffset==1:
					self.menu.play_sound(self.sounds["noise.wav"])
				#first 30 frames
				if self.johnsonOffset<30:
					if self.johnsonOffset%8>4:
						screen.blit(self.communicationCall.render("Incoming call", True, (255,255,255)),(20, 15))
				elif self.johnsonOffset<=200:
					screen.blit(self.single_sprites['johnson.png'],(10, 10))
					if self.johnsonOffset>=30:
						screen.blit(self.communication.render(self.textline1[:(self.johnsonOffset-30)*len(self.textline1)/30], True, (255,255,128)),(114, 26))
					#next 60 ones
					if self.johnsonOffset>=70:
						screen.blit(self.communication.render(self.textline2[:(self.johnsonOffset-70)*len(self.textline2)/30], True, (255,255, 128)),(114, 44))
					if self.johnsonOffset>=100:
						screen.blit(self.communication.render(self.textline3[:(self.johnsonOffset-100)*len(self.textline3)/30], True, (255,255, 128)),(114, 44+18))
					if self.johnsonOffset>=150:
						screen.blit(self.communication.render(self.textline4[:(self.johnsonOffset-150)*len(self.textline4)/30], True, (255,255, 128)),(114, 44+18+18))
					
				else:
					if self.johnsonOffset == 200:
						self.menu.play_sound(self.sounds["noise.wav"])
					if self.johnsonOffset%8>4:
						screen.blit(self.communicationCall.render("Transmission end", True, (255,255,255)),(20, 15))				
		return level
		
		
		
		
		
		
		
		
		
