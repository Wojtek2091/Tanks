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
    neutralGroup, enemyGroup, playerGroup, bushGroup, plateGroup = buildMap("E           E            E"
                                                                            "                          "
                                                                            "                          "
                                                                            "        XXXXXXXXX         "
                                                                            "        XXXXEXXXX         "
                                                                            "        XXXXEXXXX         "
                                                                            "        XXXXXXXXX         "
                                                                            "        BBBBBBBBB         "
                                                                            "        X                 "
                                                                            "                          "
                                                                            "   LLLLLLLLLLLLLL         "
                                                                            "   LLLLLLLLLLLLLL         "
                                                                            "         S                "
                                                                            "     P    L               ", B, W, H)
    bulletGroup = pygame.sprite.Group([])
    boomGroup = pygame.sprite.Group([])
    groupsList = [playerGroup, neutralGroup, enemyGroup, bulletGroup, boomGroup, bushGroup, plateGroup,]
    return groupsList


# Funkcja ta na pdstawie stringa buduje mape levela
# X-birckblock E-enemy P-palyer [sapce] -nic
def buildMap(toParse, BLOCKSIZE, WIDTH, HEIGHT):
    x = 0
    y = 0
    neutralGroup = pygame.sprite.Group([])
    enemyGroup = pygame.sprite.Group([])
    playerGroup = pygame.sprite.Group([])
    bushGroup = pygame.sprite.Group([])
    plateGroup = pygame.sprite.Group([])
    bricksImg = pygame.image.load('Sprites/bricks.png')
    enemy1Img = pygame.image.load('Sprites/enemy1.png')
    enemy12Img = pygame.image.load('Sprites/enemy12.png')
    bulletImg = pygame.image.load('Sprites/bullet.png')
    bushImg = pygame.image.load('Sprites/bush.png')
    plateImg = pygame.image.load('Sprites/plate.png')
    for ch in toParse:
        if ch == "X":
            neutralGroup.add(NormalBricksBlock(x, y, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 25, y, bricksImg))
            neutralGroup.add(NormalBricksBlock(x, y + 25, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 25, y + 25, bricksImg))
        elif ch == "S":
            neutralGroup.add(NormalBricksBlock(x + 25, y + 25, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 50, y + 25, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 75, y + 25, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 100, y + 25, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 25, y + 50, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 25, y + 75, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 100, y + 50, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 100, y + 75, bricksImg))

        elif ch == "B":
            bushGroup.add(Bush(x, y, bushImg))
            bushGroup.add(Bush(x + 25, y, bushImg))
            bushGroup.add(Bush(x, y + 25, bushImg))
            bushGroup.add(Bush(x + 25, y + 25, bushImg))
        elif ch == "E":
            enemyGroup.add(Enemy(x, y, enemy1Img, enemy1Img, enemy12Img, 10, 1, bulletImg, 1))
        elif ch == "L":
            plateGroup.add(Plate(x, y, plateImg))
        elif ch == "P":
            playerGroup.add(pygame.sprite.Group([Player(x, y, pygame.image.load('Sprites/player.png'), pygame.image.load('Sprites/player.png'), pygame.image.load('Sprites/player2.png'), 100, 2, pygame.image.load('Sprites/bullet.png'), 1)]))
        if (x + BLOCKSIZE) >= WIDTH:
            x = 0
            y += BLOCKSIZE
        else:
            x += BLOCKSIZE
    return neutralGroup, enemyGroup, playerGroup, bushGroup,  plateGroup
