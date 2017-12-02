from Objects import *

# level bulder buduje mape  levelu na podstawie zadanego Stringa


def buildLevel():
    bricksImg = pygame.image.load('Sprites/bricks.png')
    playerGroup = pygame.sprite.Group([Player(600, 600, pygame.image.load('Sprites/player.png'), 100, 5, pygame.image.load('Sprites/bullet.png'), 1)])
    neutralGroup = pygame.sprite.Group([NormalBricksBlock(200, 200, bricksImg), NormalBricksBlock(225, 200, bricksImg), NormalBricksBlock(200, 225, bricksImg), NormalBricksBlock(225, 225, bricksImg)])
    enemyGroup = pygame.sprite.Group([])
    bulletGroup = pygame.sprite.Group([])
    groupsList = [playerGroup, neutralGroup, enemyGroup, bulletGroup]
    return groupsList

