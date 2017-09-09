# handles the smoke present at the screen at this time
import random
import common_pygame
import load_resources

single_sprites = load_resources.single_sprites
pygame = common_pygame.pygame
screen = common_pygame.screen

smokes = list()

# size : 1 : asteroids, 2: ships, 3: boss


def addSmoke(x, y, size):
    # appending the smoke particle, and his current life (300
    #size = random.randint(10,45)
    # size=45
    smokes.append((x, y, 256, size))


def determine_smoke(k):
    (x, y, life, size) = k
    #print("life:", life)
    if life >= 0:
        return True
    return False


def blitAndUpdate():
    for i in range(len(smokes)):
        # delete the particles that are too old
        smokes[:] = [k for k in smokes if determine_smoke(k)]
        for i in range(len(smokes)):
            # blit the concerned particle
            (x, y, life, size) = smokes[i]
            life = life - 1

            if size > 0 and life % 8 == 0:
                size = size - 1
            #print("size", size)
            toblit = pygame.transform.scale(
                single_sprites['smoke.png'], (size, size))
            screen.blit(toblit, (x - (25 - size), y - (25 - size)))

            smokes[i] = (x, y, life, size)
