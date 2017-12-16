from Objects import *
lvlch="XXXXXXXXXXXXXXXXXXXXXXXXXX" \
      "XXXXXXXXXX     XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXXXXX XXX XXXXXXXXXXX" \
      "XXXXXXX    XXX    XXXXXXXX" \
      "XXXXXXX XXXXXXXXX XXXXXXXX" \
      "XXXXXXX XXXXXXXXX XXXXXXXX" \
# level bulder przygotowyje lvl
def buildLevel(B, W, H):
    bricksImg = pygame.image.load('Sprites/bricks.png')
    neutralGroup, enemyGroup, playerGroup = buildMap("EXXXXXX  EXXXXE   XXXXXXXE"
                                                     "        XXXEXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "        XXXXXXXXX         "
                                                     "           P              ", B, W, H)
    bulletGroup = pygame.sprite.Group([])
    boomGroup = pygame.sprite.Group([])
    groupsList = [playerGroup, neutralGroup, enemyGroup, bulletGroup, boomGroup]
    return groupsList


# Funkcja ta na pdstawie stringa buduje mape levela
# X-birckblock [sapce] -nic
def buildMap(toParse, BLOCKSIZE, WIDTH, HEIGHT):
    x = 0
    y = 0
    neutralGroup = pygame.sprite.Group([])
    enemyGroup = pygame.sprite.Group([])
    playerGroup = pygame.sprite.Group([])
    bricksImg = pygame.image.load('Sprites/bricks.png')
    enemyImg = pygame.image.load('Sprites/enemy1.png')
    bulletImg = pygame.image.load('Sprites/bullet.png')
    for ch in toParse:
        if ch == "X":
            neutralGroup.add(NormalBricksBlock(x, y, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 25, y, bricksImg))
            neutralGroup.add(NormalBricksBlock(x, y + 25, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 25, y + 25, bricksImg))
        elif ch == "E":
            enemyGroup.add(Enemy(x, y, enemyImg, 4, 1, bulletImg, 1))
        elif ch == "P":
            playerGroup.add(pygame.sprite.Group([Player(x, y, pygame.image.load('Sprites/player.png'), 1000, 4, pygame.image.load('Sprites/bullet.png'), 1)]))
        if (x + BLOCKSIZE) >= WIDTH:
            x = 0
            y += BLOCKSIZE
        else:
            x += BLOCKSIZE
    return neutralGroup, enemyGroup, playerGroup
