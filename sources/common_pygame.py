import pygame, sys, pygame.mixer
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
#pygame.mouse.set_visible(0)
pygame.mixer.set_num_channels(32)
pygame.display.set_caption("MICshooter")

screenwidth=screen.get_width()
screenheight=screen.get_width()
