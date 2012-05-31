import os
import common_pygame
import sprite_handling
import menu

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
	#loading sounds
	#sounds is a dict that contains all the sounds
	#global pygame = pygame_arg
	
	add_sound("laser.wav")
	add_sound("laser2.wav")
	add_sound("laser3.wav")
	add_sound("laser4.wav")
	add_sound("laser5.wav")
	add_sound("explosion.wav")
	add_sound("explosion2.wav")
	add_sound("life.wav")
	add_sound("ouch.wav")
	add_sound("loser.wav")
	add_sound("shield1.wav")
	add_sound("armor.wav")
	add_sound("plasma1.wav")
	add_sound("plasmagun.wav")
	#single_sprites is a dict that contains all the single sprites
	
	add_sprite("sprite_ship.png")
	add_sprite("sprite_ship_fire.png")
	add_sprite("sprite_ship_weapon2.png")
	add_sprite("sprite_laser.png")
	add_sprite("sprite_laser_blue.png")
	add_sprite("sprite_lasershoot.png")
	add_sprite("sprite_enemy.png")
	add_sprite("sprite_enemy_fire.png")
	add_sprite("background.png")
	#add_sprite("stars.png")
	add_sprite("backgroundtransp.png")
	add_sprite("asteroid1.png")
	add_sprite("asteroid2.png")
	add_sprite("asteroid3.png")
	add_sprite("planet1.png")
	add_sprite("planet2.png")
	add_sprite("planet3.png")
	add_sprite("lifebonus.png")
	add_sprite("armorbonus.png")
	add_sprite("lifeBonusRing.png")
	add_sprite("armorBonusRing.png")
	add_sprite("lifemask.png")
	add_sprite("ball1.png")
	
	
	#light
	add_sprite("sprite_laser_blue_light.png")
	add_sprite("sprite_laser_light.png")
	add_sprite("ball1_light.png")
	add_sprite("lifeBonusLight.png")
	
	#menu
	add_sprite("menu_micshooter.png")
	add_sprite("menu_options.png")
	add_sprite("menu_optionsblurry.png")
	add_sprite("menu_play.png")
	add_sprite("menu_playblurry.png")
	add_sprite("menu_resume.png")
	add_sprite("menu_resumeblurry.png")
	add_sprite("menu_quit.png")
	add_sprite("menu_quitblurry.png")
	add_sprite("menu_sound.png")
	add_sprite("menu_on.png")
	add_sprite("menu_off.png")
	add_sprite("menu_resolution.png")
	add_sprite("menu_800600.png")
	add_sprite("menu_800500.png")
	#loading sprite sequences
	#sprite_explosion_list = sprite_handling.load_sliced_sprites(pygame, 64, 64, "explosion_sheet.png" )
	add_sprite_sequence("sprite_explosion_list.png", 192, 192)
	add_sprite_sequence("sprite_explosion_list_asteroid.png", 192, 192)
	return (sounds, single_sprites, sprite_sequences)
