import os
import common_pygame
import random
import collisions
pygame = common_pygame.pygame
screen = common_pygame.screen


class Asteroids():

    def __init__(self, single_sprites):
        self.single_sprites = single_sprites
        self.compteur = 0
        self.asteroidList = list()
        self.rotateAst = 0

    def updatecompteur(self):
        self.compteur = self.compteur + 1

    def determine(self, x):
        (x_, y, v, s, sprite, h, w) = x
        if y - h >= screen.get_height():
            return True
        return False

    def blitAsteroids(self, laserlist):
        if len(self.asteroidList) <= 2 and self.compteur % 10 == 0:
            #x, y, speed, size, sprite, height
            size = random.randrange(10, 150)

            asteroid = False
            # load the appropriate sprite
            choix = random.randrange(1, 7)
            if choix == 1:
                spritearg = pygame.transform.scale(
                    self.single_sprites['asteroid1.png'], (size, size)).convert_alpha()
            elif choix == 2:
                spritearg = pygame.transform.scale(
                    self.single_sprites['asteroid3.png'], (size, size)).convert_alpha()
            else:
                spritearg = pygame.transform.scale(
                    self.single_sprites['asteroid2.png'], (size, size)).convert_alpha()

            speed = random.randrange(7, 12)

            height = spritearg.get_height()
            width = spritearg.get_width()
            self.asteroidList.append((random.randrange(
                0, screen.get_width()), 0, speed, size, spritearg, height, width))

        # determine : false if keep, true if delete
        self.asteroidList[:] = [
            x for x in self.asteroidList if not self.determine(x)]

        for index in xrange(len(self.asteroidList)):
            # verify if a laser is not touching the asteroid

            (x, y, v, s, sprite, h, w) = self.asteroidList[index]
            screen.blit(sprite, (x, y - h))
            y = y + v
            self.asteroidList[index] = (x, y, v, s, sprite, h, w)
