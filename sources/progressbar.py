import os
import common_pygame
import random
pygame = common_pygame.pygame
screen = common_pygame.screen


class progressBar():

    def __init__(self):
        self.color = (102, 170, 255)
        self.y1 = screen.get_height() / 2
        self.y2 = self.y1 + 20
        self.max_width = 800 - 40
        self.font = pygame.font.Font("BITSUMIS.TTF", 64)
        self.loading = self.font.render("LOADING", True, self.color)
        self.textHeight = self.y1 - 80

    def update(self, percent):
        screen.fill((0, 0, 0))

        screen.blit(self.loading, (300, self.textHeight))
        txtpercent = self.font.render(str(percent) + "%", True, self.color)
        screen.blit(txtpercent, (20, self.y1 + 30))
        pygame.draw.rect(screen, self.color,
                         (20, self.y1, self.max_width, 20), 2)
        pygame.draw.rect(screen, self.color, (20, self.y1,
                                              (percent * self.max_width) / 100, 20), 0)
        pygame.display.flip()

        (r, g, b) = self.color
        r = min(r + 2, 255)
        g = max(g - 2, 0)
        b = max(b - 2, 0)
        self.color = (r, g, b)
        self.loading = self.font.render("LOADING", True, self.color)
