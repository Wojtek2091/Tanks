from Objects import *

# level bulder buduje mape  levelu na podstawie zadanego Stringa


def buildLevel():
    bricksImg = pygame.image.load('Sprites\\bricks.png')
    playerGroup = pygame.sprite.Group([Player(600, 600, pygame.image.load('Sprites\\tank1.png'), 100, 5, pygame.image.load('Sprites\\bullet.png'), 1)])
    neutralGroup = pygame.sprite.Group([NormalBricksBlock(200, 200, bricksImg)])
    enemyGroup = pygame.sprite.Group([])
    bulletGroup = pygame.sprite.Group([])
    groupsList = [playerGroup, neutralGroup, enemyGroup, bulletGroup]
    return groupsList

