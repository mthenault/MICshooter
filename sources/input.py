import common_pygame
pygame = common_pygame.pygame
screen = common_pygame.screen


def keyInput():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # print(pygame.key.name(event.key))
            # return ""
            return pygame.key.name(event.key)
        else:
            return False
