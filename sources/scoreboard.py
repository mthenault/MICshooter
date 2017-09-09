import common_pygame
import load_resources
import os
import pickle
import operator


pygame = common_pygame.pygame
screen = common_pygame.screen


class ScoreBoard():

    # init the score object
    def __init__(self):
        # empty score list
        self.scores = list()
        self.scorefont = pygame.font.Font("BITSUMIS.TTF", 30)
        # fill the score list with the existing file if it exists
        if os.path.exists(os.path.join('data', 'scores.txt')):
            with open(os.path.join('data', 'scores.txt'), 'rb') as fichier:
                depickler = pickle.Unpickler(fichier)
                self.scores = depickler.load()

    def addScore(self, score, name):
        # append the new score into the list
        self.scores.append((score, name))
        # sort the list by score :
        self.scores = sorted(
            self.scores, key=operator.itemgetter(0), reverse=True)
        # write the config into the file
        with open(os.path.join('data', 'scores.txt'), 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(self.scores)

    def printScore(self):
        # print(self.scores)
        # print the background rectangle
        s = pygame.Surface((500, 310))  # the size of your rect
        s.set_alpha(64)                # alpha level
        s.fill((99, 0, 201))           # this fills the entire surface
        screen.blit(s, (150, 210))    # (0,0) are the top-left coordinates

        max = len(self.scores)

        for i in range(min(max, 10)):
            (score, name) = self.scores[i]
            screen.blit(self.scorefont.render(str(name), True,
                                              (255, 255, 255)), (160, 220 + i * 30))
            screen.blit(self.scorefont.render(str(score), True,
                                              (255, 255, 255)), (450, 220 + i * 30))
