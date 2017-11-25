from Objects import *

# level bulder buduje mape  levelu na podstawie zadanego Stringa


def buildLevel():
    bricksImg = pygame.image.load('Sprites\\bricks.png')
    playerGroup = pygame.sprite.Group([Player(600, 600, pygame.image.load('Sprites\\tank1.png'), 100, 5)])
    neutralGroup = pygame.sprite.Group([NormalBricksBlock(200, 200, bricksImg)])
    groupsList = [playerGroup, neutralGroup]
    return groupsList

