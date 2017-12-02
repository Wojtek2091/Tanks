from LevelBuilder import *


# GameHandler iteruje po każdej grupie Spritów w lście i wywołuche ich metody render i update
class GameHandler:
    # groups: 0-player 1-neutral, 2-enemy, 3-bullets
    def __init__(self,disaplysurface, groupsList = None):
        self.displaysurface = disaplysurface
        if groupsList is None:
            self.groupsList = []
        else:
            self.groupsList = groupsList

    def update(self):
        self.groupsList[0].update(self, self.groupsList[1])
        self.groupsList[1].update(self.groupsList[3], self.groupsList[1])
        self.groupsList[3].update()

    def render(self, displaysurface):
        for group in self.groupsList:
            group.draw(displaysurface)

    def addBullet(self, bullet):
        self.groupsList[3].add(bullet)


def main():
    WIDTH=1280
    HEIGHT=720
    FPS = 60  # frames per second
    fpsClock = pygame.time.Clock()
    pygame.init()
    DISPLAYSURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tanki!')
    gameHandler = GameHandler(DISPLAYSURFACE, buildLevel())
    while True:  # główna pętla
        DISPLAYSURFACE.fill((140, 140, 140))
        gameHandler.render(DISPLAYSURFACE)
        gameHandler.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


main()