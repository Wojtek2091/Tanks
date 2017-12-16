import pygame
from pygame.locals import *
from LevelBuilder import buildLevel


# GameHandler iteruje po każdej grupie Spritów w lście i wywołuche ich metody render i update
class GameHandler:
    # groups: 0-player 1-neutral, 2-enemy, 3-bullets, 4-boom
    def __init__(self,disaplysurface, groupsList = None):
        self.displaysurface = disaplysurface
        if groupsList is None:
            self.groupsList = []
        else:
            self.groupsList = groupsList

    def update(self):
        self.groupsList[0].update(self, self.groupsList)
        self.groupsList[2].update(self, self.groupsList)
        self.groupsList[3].update(self.groupsList)
        self.groupsList[4].update(self.groupsList)

    def render(self, displaysurface):
        for group in self.groupsList:
            group.draw(displaysurface)

    def addBullet(self, bullet):
        self.groupsList[3].add(bullet)

BLOCKSIZE=50
WIDTH=1300
HEIGHT=700

def main():

    FPS = 60  # frames per second
    fpsClock = pygame.time.Clock()
    pygame.init()
    DISPLAYSURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tanki!')
    gameHandler = GameHandler(DISPLAYSURFACE, buildLevel(BLOCKSIZE, WIDTH, HEIGHT))
    while True:  # główna pętla
        DISPLAYSURFACE.fill((140, 140, 140))
        gameHandler.render(DISPLAYSURFACE)
        gameHandler.update()
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


main()