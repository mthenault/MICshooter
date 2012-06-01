import os
import common_pygame
import random
pygame = common_pygame.pygame
screen= common_pygame.screen
clock= common_pygame.clock

def fadeToColor(r, g, b):
	animlen=150
	for i in range(0, animlen, 5):
		clock.tick_busy_loop(30)
		screen.fill(((255-r)*i/animlen,(255-g)*i/animlen,(255-b)*i/animlen), special_flags=pygame.BLEND_SUB)
		pygame.display.flip()

#def fadeFromBlack():
	#animlen=255
	#for i in range(0, animlen, 5):
		#clock.tick_busy_loop(30)
		#screen.fill((i, \
		#i,\
		#i),\
		 #special_flags=pygame.BLEND_MIN)
		#pygame.display.flip()
