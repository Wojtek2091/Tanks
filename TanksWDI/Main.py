import pygame, sys
from pygame.locals import *
from LevelBuilder import buildLevel
from Objects import Menu, Button


# GameHandler iteruje po każdej grupie Spritów w lście i wywołuche ich metody render i update
class GameHandler:
    # groups: 0-player 1-neutral, 2-enemy, 3-bullets, 4-boom 5-bushes , 6-plates
    def __init__(self, disaplysurface, gameover, groupsList = None):
        self.displaysurface = disaplysurface
        self.gameover = gameover
        if groupsList is None:
            self.groupsList = []
        else:
            self.groupsList = groupsList

    def update(self):
        self.groupsList[0].update(self, self.groupsList)
        self.groupsList[2].update(self, self.groupsList)
        self.groupsList[3].update(self.groupsList)
        self.groupsList[4].update(self.groupsList, self.gameover)

    def render(self, displaysurface):
        self.groupsList[6].draw(displaysurface)
        self.groupsList[0].draw(displaysurface)
        self.groupsList[1].draw(displaysurface)
        self.groupsList[2].draw(displaysurface)
        self.groupsList[3].draw(displaysurface)
        self.groupsList[4].draw(displaysurface)
        self.groupsList[5].draw(displaysurface)


    def addBullet(self, bullet):
        self.groupsList[3].add(bullet)


BLOCKSIZE = 50
WIDTH = 1300
HEIGHT = 700
DISPLAYSURFACE = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    inMenu = True
    FPS = 60  # frames per second
    fpsClock = pygame.time.Clock()
    pygame.init()

    pygame.display.set_caption('Tanki!')
    menu = Menu()
    menu.addButton(Button(535, 100, pygame.image.load('Sprites/Menu/bs1.png'), pygame.image.load('Sprites/Menu/bs2.png'),
                   pygame.image.load('Sprites/Menu/bs3.png'), "start", play))
    menu.addButton(Button(535, 200, pygame.image.load('Sprites/Menu/be1.png'), pygame.image.load('Sprites/Menu/be2.png'),
                   pygame.image.load('Sprites/Menu/be3.png'), "start", sys.exit))

    while inMenu: # pętla menu
        DISPLAYSURFACE.fill((70, 70, 70))
        menu.update(DISPLAYSURFACE)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


def play():
    FPS = 60  # frames per second
    fpsClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Tanki!')
    gameHandler = GameHandler(DISPLAYSURFACE, gameover, buildLevel(BLOCKSIZE, WIDTH, HEIGHT))
    while True:  # główna pętla
        DISPLAYSURFACE.fill((0, 0, 0))
        gameHandler.render(DISPLAYSURFACE)
        gameHandler.update()
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)

def gameover():
    FPS = 60  # frames per second
    fpsClock = pygame.time.Clock()
    pygame.init()
    clip = Menu ()
    clip.addButton(Button(250, 100, pygame.image.load('Sprites/Menu/go.png'), pygame.image.load('Sprites/Menu/go.png'),
                    pygame.image.load('Sprites/Menu/go.png'), "go"))
    clip.addButton(Button(535, 300, pygame.image.load('Sprites/Menu/bs1.png'), pygame.image.load('Sprites/Menu/bs2.png'),
                    pygame.image.load('Sprites/Menu/bs3.png'), "start", play))
    clip.addButton(Button(535, 400, pygame.image.load('Sprites/Menu/be1.png'), pygame.image.load('Sprites/Menu/be2.png'),
                    pygame.image.load('Sprites/Menu/be3.png'), "start", sys.exit))
    while True:
        DISPLAYSURFACE.fill((70, 70, 70))
        clip.update(DISPLAYSURFACE)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)

main()