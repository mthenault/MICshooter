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
	
def	updateProgbar(percent,x1,  y1,max_width, color, color2):
	#s = pygame.Surface((1000,750))  # the size of your rect
	#s.set_alpha(128)                # alpha level
	#s.fill((255,255,255))           # this fills the entire surface
	#windowSurface.blit(s, (0,0))    # (0,0) are the top-left coordinates

	#s = pygame.Surface((1000,750))  # the size of your rect
	#s.set_alpha(128)                # alpha level
	#s.fill((255,255,255))           # this fills the entire surface
	#windowSurface.blit(s, (0,0))    # (0,0) are the top-left coordinates
	
	#txtpercent = self.font.render(str(percent)+"%", True, self.color)
	#screen.blit(txtpercent, (20,y1+30))
	pygame.draw.rect(screen, color, (x1,y1,(percent*max_width)/100,15), 0)
	pygame.draw.rect(screen,  color2, (x1,y1,max_width,15), 1 )



class Hud():
	def __init__(self, single_sprites):
		self.single_sprites=single_sprites
			# Create a font
		self.tinyfont = pygame.font.Font(None, 16)
		self.font = pygame.font.Font(None,32)
		self.font2 = pygame.font.Font(None, 150)
		self.score_label = self.tinyfont.render("score", True, (255,255, 0))
		self.inf = self.font.render("Inf.", True, (0,130, 255))
		
		self.offset=0
		
	def blit(self, ship, level):
			# Render the text
		#life_txt = self.font.render(str(ship.life), True, (255,0, 0))
		score_txt = self.font.render(str(ship.score), True, (255,255, 255))
		#armor_txt = self.font.render(str(ship.armor), True, (255,255, 0))
		level_txt = self.tinyfont.render("level " + str(level), True, (255,255, 0))
		#show the HUD
		screen.blit(self.single_sprites['lifemask.png'],(0,
		600-self.single_sprites['lifemask.png'].get_height() -self.offset))
		#show the life and the score
		#screen.blit(life_txt, (common_pygame.screenwidth-70,common_pygame.screenheight-224 -self.offset))
		screen.blit(self.score_label, (350-35,common_pygame.screenheight-215 -self.offset))
		screen.blit(score_txt, (350,common_pygame.screenheight-224-self.offset ))
		screen.blit(level_txt, (455,common_pygame.screenheight-215 -self.offset))
		
		
		
		#progress bar for the armor
		updateProgbar(ship.armor,25,  common_pygame.screenheight-223, 150, (7,200,0), (7,200,0))
		screen.blit(self.single_sprites['armorbonus.png'],(0,common_pygame.screenheight-232))
		
		#progress bar for the life
		updateProgbar(ship.life,common_pygame.screenwidth-25-150,  common_pygame.screenheight-223, 150, (0,181,200), (0,181,200))
		screen.blit(self.single_sprites['lifebonus.png'],(common_pygame.screenwidth-25,common_pygame.screenheight-232))		
		
		#screen.blit(armor_txt, (35,common_pygame.screenheight-227-self.offset ))
		
		#blit the current weapon and the ammo
		if ship.weapon==1:
			
			screen.blit(self.single_sprites['sprite_laser.png'],(160+50, common_pygame.screenheight-220 -self.offset))
			screen.blit(self.inf,(185+50, common_pygame.screenheight-227 -self.offset))
		else:
			ammo_txt = self.font.render(str(ship.ammo), True, (0,130, 255))
			screen.blit(self.single_sprites['ball1.png'],(160+50, common_pygame.screenheight-220-self.offset ))
			screen.blit(ammo_txt,(185+50, common_pygame.screenheight-227 -self.offset))
