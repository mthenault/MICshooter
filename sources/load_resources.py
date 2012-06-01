import os
import common_pygame
import sprite_handling
import menu
import progressbar

pygame = common_pygame.pygame
sounds = dict()
single_sprites = dict()
sprite_sequences = dict()


def add_sound(soundfile):
	global sounds
	sounds[soundfile] = pygame.mixer.Sound(os.path.join('sounds', soundfile))
	sounds[soundfile].set_volume(0.5)
	
def add_sprite(spritefile):
	global single_sprites
	single_sprites[spritefile]=pygame.image.load(os.path.join('images',spritefile)).convert_alpha()
	single_sprites[spritefile].set_colorkey((255,0,255))
	

def add_sprite_sequence(spritesequence, h, w):
	global sprite_sequences 
	sprite_sequences[spritesequence]= \
	sprite_handling.load_sliced_sprites( w, h, spritesequence )

def load_resources(pygame_arg):
	prog = progressbar.progressBar()
	#loading sounds
	#sounds is a dict that contains all the sounds
	#global pygame = pygame_arg
	prog.update(0)
	soundlist=["laser.wav", "laser2.wav", "laser3.wav", "laser4.wav","laser5.wav", \
	 "explosion.wav", "explosion2.wav", "life.wav", "ouch.wav", "loser.wav", "shield1.wav", \
	 "armor.wav", "plasma1.wav", "plasmagun.wav"]
	 
	for index in xrange (len(soundlist)):
		 add_sound(soundlist[index])
		 prog.update(index*40/len(soundlist))
	
	sprite_load_list=["sprite_ship.png","sprite_ship_fire.png",  "sprite_ship_weapon2.png", \
	"sprite_laser.png", "sprite_laser_blue.png", "sprite_lasershoot.png","sprite_enemy.png", \
	"sprite_enemy_fire.png", "background.png","backgroundtransp.png", "asteroid1.png", \
	 "asteroid2.png", "asteroid3.png", "planet1.png", "planet2.png", "planet3.png", \
	 "lifebonus.png", "armorbonus.png", "lifeBonusRing.png", "armorBonusRing.png", \
	 "lifemask.png", "ball1.png", "sprite_laser_blue_light.png","sprite_laser_light.png", \
	  "ball1_light.png","lifeBonusLight.png","menu_micshooter.png", "menu_options.png",
	 "menu_optionsblurry.png", "menu_play.png","menu_playblurry.png","menu_resume.png", \
	  "menu_resumeblurry.png",  "menu_quit.png", "menu_quitblurry.png","menu_sound.png", \
	   "menu_on.png", "menu_off.png","menu_resolution.png","menu_800600.png", "menu_800500.png"      ]
	
	for index in xrange (len(sprite_load_list)):
		 add_sprite(sprite_load_list[index])
		 prog.update((index*60/len(sprite_load_list))+40)
	
	
	
	#loading sprite sequences
	#sprite_explosion_list = sprite_handling.load_sliced_sprites(pygame, 64, 64, "explosion_sheet.png" )
	add_sprite_sequence("sprite_explosion_list.png", 192, 192)
	add_sprite_sequence("sprite_explosion_list_asteroid.png", 192, 192)
	prog.update(100)
	return (sounds, single_sprites, sprite_sequences)

