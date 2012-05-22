#w : image width
#h : image height
#filename :name of the file
import os
import common_pygame
pygame = common_pygame.pygame

def load_sliced_sprites(w, h, filename):
	
	images = []
	
	master_image = pygame.image.load(os.path.join('images', filename)).convert_alpha()
	master_width, master_height = master_image.get_size()

	columns = master_width/w
	rows =master_height/h
	print(master_width, master_height, columns, rows)
	for i in xrange (rows):
		for j in xrange (columns):
			print(j*w,i*h,w,h)
			cursurf = master_image.subsurface((j*w,i*h,w,h))
			cursurf.set_colorkey((255,0,255))
			images.append(cursurf)

	return images
