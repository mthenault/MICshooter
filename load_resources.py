import os
import common_pygame
import sprite_handling

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
	add_sound("explosion.wav")
	add_sound("explosion2.wav")
	add_sound("life.wav")
	add_sound("ouch.wav")
	add_sound("loser.wav")
	add_sound("shield1.wav")
	#single_sprites is a dict that contains all the single sprites
	
	add_sprite("sprite_ship.png")
	add_sprite("sprite_laser.png")
	add_sprite("sprite_laser_blue.png")
	add_sprite("sprite_lasershoot.png")
	add_sprite("sprite_enemy.png")
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
	add_sprite("lifeBonusRing.png")
	add_sprite("lifemask.png")
	#loading sprite sequences
	#sprite_explosion_list = sprite_handling.load_sliced_sprites(pygame, 64, 64, "explosion_sheet.png" )
	add_sprite_sequence("sprite_explosion_list.png", 192, 192)
	add_sprite_sequence("sprite_explosion_list_asteroid.png", 192, 192)
	return (sounds, single_sprites, sprite_sequences)

